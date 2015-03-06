#!/usr/bin/python
import sys
import threading
import time
import gc
import traceback
import smtplib
import socket
import logging
import logging.config
import ConfigParser
from email import utils
import optparse
from datetime import datetime
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

from easyprocess import EasyProcessCheckInstalledError
from PHPDemoApp import PHPDemoApp
from MovieDemoApp import MovieDemoApp
from EcomApp import EcomApp
from MailAlert import MailAlert
from StreamToLogger import StreamToLogger


class SeleniumThread(threading.Thread): 

    def __init__(self,demoapp,browser,url,useragent, continuous_session):
        self.demoapp = demoapp
        self.browser = browser
        self.url = url
        self.useragent = useragent
        self.continuous_session = continuous_session
        self.display = ""
        self.mailAlert = MailAlert('demouser@appdynamics.com','smtp.googlemail.com','demouser@appdynamics.com','d3m0Password')
        self.receiveEmailAlerts = 'trabaut@appdynamics.com'
        self.selenium_logger = logging.getLogger('selenium_logger')
        threading.Thread.__init__(self)

    def run(self): 
        try:
            if self.demoapp == "PHPDemoApp": 
                app = PHPDemoApp(self.browser, self.useragent, self.url, self.continuous_session)
                app.run()
            elif self.demoapp == "EcomApp":
                app = EcomApp(self.browser, self.useragent, self.url, self.continuous_session)
                app.run()
            elif self.demoapp == "MovieDemoApp": 
                app = MovieDemoApp(self.browser, self.useragent, self.url, self.continuous_session)
                app.run()
        except EasyProcessCheckInstalledError as epciError: 
            self.selenium_logger.error('Xvfb is not installed. Unable to start Virtual Display')
            self.mailAlert.sendMail(self.receiveEmailAlerts,'Selenium Error', 'Xvfb is not installed. Unable to start Virtual Display')
        except Exception as e: 
            self.selenium_logger.error('Unexpected Error %s:%s', self.demoapp, sys.exc_info()[0])
            traceback.print_exc()
            #traceback.print_tb(sys.exc_info()[2], file=sys.stdout)
            message = 'Unexpected Error %s:%s\n\n' % (self.demoapp, sys.exc_info()[0])
            message += 'URL = %s\n' % self.url
            message += '%s\n' % sys.exc_info()[1]
            message += '%s\n' % sys.exc_info()[2]
            self.mailAlert.sendMail(self.receiveEmailAlerts,'Selenium Error', message)
            #app.run()

parser = optparse.OptionParser('usage SeleniumDemoLoad -c <configuration file>')
parser.add_option('-c', dest='config', type='string', help='specify configuration file')
(options, args) = parser.parse_args()

config = options.config

if config == None:
    print parser.usage
    exit(0)

settings = list()
setting = list()
lineNum=0

configFile = ConfigParser.RawConfigParser()
configFile.read(config)
sections = configFile.sections()

stdoutmutex = threading.Lock()
threads = []

loggingconfig = configFile.items('Logging')
logfilelocation = loggingconfig[0][1]
loglevel = loggingconfig[1][1]

# setting up logging
selenium_logger = logging.getLogger('selenium_logger')
if loglevel == 'DEBUG':
    selenium_logger.setLevel(logging.DEBUG)
elif loglevel == 'INFO':
    selenium_logger.setLevel(logging.INFO)
elif loglevel == 'WARNING':
    selenium_logger.setLevel(logging.WARNING)
elif loglevel == 'ERROR':
    selenium_logger.setLevel(logging.ERROR)
elif loglevel == 'CRITICAL':
    selenium_logger.setLevel(logging.CRITICAL)
configFilename = config.split('/')[len(config.split('/'))-1]
logfilename = logfilelocation + '/' + configFilename + '.log'
log_handler = logging.handlers.RotatingFileHandler(logfilename, maxBytes=5000000, backupCount=5)
log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log_handler.setFormatter(log_formatter)
selenium_logger.addHandler(log_handler)
selenium_logger.info('Starting Selenium Demo Load')

StreamToLogger.addHandler(log_handler)
StreamToLogger.setLevel(logging.INFO)
sys.stderr = StreamToLogger

browserconfig = configFile.items('Browser')
continuous_session_config = browserconfig[0][1]

if continuous_session_config == 'False':
    continuous_session = False
elif continuous_session_config == 'True':
    continuous_session = True
else:
    selenium_logger.error('ContinuousSession must be set to either True or False')


for section in sections:
    if (section != 'Logging') & (section != 'Browser'):
        myvars = {}
        items = configFile.items(section)
        for item in items:
            myvars[item[0]] = item[1]
        selenium_logger.info('%s = %s', section, myvars)
        thread = SeleniumThread(myvars['demoapp'], myvars['browser'], myvars['url'], myvars['useragent'], continuous_session)
        thread.start()
        threads.append(thread)

for thread in threads:
    thread.join()

selenium_logger.info('Main thread exiting')





