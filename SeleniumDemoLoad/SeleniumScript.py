import sys
import logging
from pyvirtualdisplay import Display
from urllib2 import URLError
from selenium import webdriver
import traceback
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

class SeleniumScript:

    def __init__(self,browser, useragent, url, continuous_session):
        self.browser = browser
        self.url = url
        self.useragent = useragent
        self.selenium_logger = logging.getLogger('selenium_logger')
        self.continuous_session = continuous_session

        if self.browser == "Firefox" or self.browser == "Chrome":
            self.display = Display(visible=0, size=(800, 600))
            self.display.start()
        
    def getDriver(self): 

        try: 
            if self.browser == "Firefox": 
                profile = webdriver.FirefoxProfile()
                profile.set_preference("general.useragent.override", self.useragent)
                return webdriver.Firefox(profile)
            elif self.browser == "PhantomJS": 
                return webdriver.PhantomJS() 
            elif self.browser == "Chrome": 
                options = Options()
                userAgent = "user-agent="+self.useragent
                options.add_argument(userAgent)
                options.add_argument("--disable-application-cache")
		options.add_argument("--no-sandbox")
                service_log_path='/tmp/chromedriver.log'
                service_args = ['--verbose']
                return webdriver.Chrome(chrome_options=options, service_args=service_args, service_log_path=service_log_path)
        except WebDriverException as wdException:
            traceback.print_exc()
            self.selenium_logger.error('WebDriverException: %s - %s - %s', self.url, wdException.message, tuple(sys.exc_info()[:2]))
            self.selenium_logger.error('%s', sys.exc_info()[0])
            self.selenium_logger.error('%s', sys.exc_info()[1])
            self.selenium_logger.error('%s', sys.exc_info()[2])
            return self.getDriver()

    def __logexception__(self, message):
        traceback.print_exc()
        self.selenium_logger.error(message)
        self.selenium_logger.error('%s', sys.exc_info()[0])
        self.selenium_logger.error('%s', sys.exc_info()[1])
        self.selenium_logger.error('%s', sys.exc_info()[2])

    def run(self): 
        
        count = 1
        max = 10
        
        # Looping through requests

        if self.continuous_session == True:
            self.driver = self.getDriver()
            self.driver.get(self.url)

        while count < max:
            try:
                if self.continuous_session == False:
                    self.driver = self.getDriver()
                    self.driver.get(self.url)
                
                self.request()
                
                if self.continuous_session == False: 
                    self.driver.close()
            except NameError as ne:
                message = 'NameError - %s - %s\n' % (self.url, ne.message)
                self.__logexception__(message)
                exit()
            except WebDriverException as wde:
                message = 'WebDriverException - %s - %s' % (self.url, wde.message)
                self.__logexception__(message)
                self.driver.close()
                self.driver = self.getDriver()
                self.driver.get(self.url)
            except NoSuchWindowException as nswe:
                message = 'NoSuchWindowException - %s - %s' % (self.url, nswe.message)
                self.__logexception__(message)
            except NoSuchElementException as nsee:
                message = 'NoSuchElement - %s - %s' % (self.url, nsee.message)
                self.__logexception__(message)
            except TimeoutException as te:
                message = 'TimeoutException - %s - %s' % (self.url, te.message)
                self.__logexception__(message)
            except URLError as ue:
                message = 'URLError - %s - %s' % (self.url, ue.message)
                self.__logexception__(message)
