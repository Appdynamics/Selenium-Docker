import smtplib
import socket
import pygeoip
from email import utils

class MailAlert():

    def __init__(self, from_address, smtpservername, username, password):

        self.from_address = from_address
        self.smtpservername = smtpservername
        self.username = username
        self.password = password
        self.gi = pygeoip.GeoIP('GeoLiteCity.dat')

    def sendMail(self, to_address, subject, message):

        Date = utils.formatdate()

        record = self.gi.record_by_name(socket.gethostbyaddr())

        subject += ' - %s, %s' % (record['city'], record['country_name'])

        text = ('From: %s\nTo: %s\nDate: %s\nSubject: %s\n\n ' % (self.from_address, to_address, Date, subject))
        text += message

        server = smtplib.SMTP_SSL(self.smtpservername,465)
        server.login(self.username, self.password)
        failed = server.sendmail(self.from_address, to_address, text)
        server.quit()

        if failed:
            print('Failed sending:', failed)
