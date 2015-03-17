import sys
import gc
import time
import random
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
from SeleniumScript import SeleniumScript

class EcomApp(SeleniumScript):

    def request(self): 

        webDriverTimeout = 60
        checkoutfrequency = 10
        pageWait = 2

        # Login
        #self.selenium_logger.info('Ecommerce Demo App: %s - %s', self.driver.title, self.url)

        # find the username and password text boxes
        w = WebDriverWait(self.driver, webDriverTimeout)
        w.until(lambda driver: self.driver.find_element_by_name('loginName'))
        loginTextBox = self.driver.find_element_by_name('loginName')
        passwordBox = self.driver.find_elements_by_id('password')
        submit = self.driver.find_elements_by_id('UserLogin_Login')

        if submit[0].is_displayed:

            # Enter username and password
            loginTextBox.send_keys('test')
            passwordBox[0].send_keys('appdynamics')
            # Submit the username and password (login)
            submit[0].click()
            time.sleep(pageWait)
            w = WebDriverWait(self.driver, webDriverTimeout)
            w.until(lambda driver: self.driver.find_element_by_id('itemsForm_submitValue'))
           
            # Find the Add To Cart button/element
            addCartButton = self.driver.find_elements_by_id('itemsForm_submitValue')
            if addCartButton[0].is_displayed:

                checkbox = self.driver.find_elements_by_name('selectedId')
                
                # print checkbox[0].get_attribute('value')
                # for element in checkbox:
                #     print element.get_attribute('value')
                # r = random.randint(1,12)
                # checkbox[r].click()


                # Determining whether or not to cause slowness in the application
                # minute = time.localtime().tm_min
                # if minute >= 0 and minute <= 20:
                #     cause_slowness = True
                #     self.selenium_logger.debug('causing slowness')
                # else:
                #     cause_slowness = False

                
                # Purchasing the Personal book which causes a slow SQL query 
                # if cause_slowness == True:
                #     self.selenium_logger.debug('Clicking Personal')
                #     checkbox[2].click()
                # else:
                #     r = random.randint(1,12)
                #     if r != 3:
                #         self.selenium_logger.debug('clicking item %d', r)
                #         checkbox[r-1].click()
                #     else:
                #         self.selenium_logger.debug('clicking item 1')
                #         checkbox[0].click()


                r = random.randint(1,12)
                self.selenium_logger.debug('clicking item %d', r)
                checkbox[r].click()

                time.sleep(pageWait)

                self.selenium_logger.debug('Clicking Add to Cart Button\n')
                addCartButton[0].click()
                time.sleep(pageWait)

                w = WebDriverWait(self.driver, webDriverTimeout)
                w.until(lambda driver: self.driver.find_element_by_id('ViewCart_submitValue'))

                # Clicking Checkout
                self.selenium_logger.debug('Clicking Checkout')
                self.driver.find_element_by_id('ViewCart_submitValue').click()
                time.sleep(pageWait)

                # r = random.randint(1,10)
                # if r == 1:
                #     # Clicking Delete from cart
                #     self.selenium_logger.debug('Clicking Delete')
                #     tags = self.driver.find_elements_by_tag_name('input')
                #     #tags[5].click()
                #     time.sleep(pageWait)
                # else:
                #     self.selenium_logger.debug('setting orderAmount')
                #     #if cause_slowness == True:
                #     #    self.driver.execute_script('document.getElementById("orderAmount").value="1"')
                #     #else:
                #     #    self.driver.execute_script('document.getElementById("orderAmount").value="1000"')
                #
                #     w = WebDriverWait(self.driver, webDriverTimeout)
                #     w.until(lambda driver: self.driver.find_element_by_id('ViewCart_submitValue'))
                #
                #     # Clicking Checkout
                #     self.driver.find_element_by_id('ViewCart_submitValue').click()
                #     time.sleep(pageWait)


                # Finding the logout button
                w = WebDriverWait(self.driver, webDriverTimeout)
                w.until(lambda driver: self.driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td/div/div/div/span'))
                logout = self.driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td/div/div/div/span')

                # Clicking logout
                logout.click()
                time.sleep(pageWait)

        #Performing garbage collection
        collected = gc.collect()
        self.selenium_logger.debug('Garbage collector: collected %d objects.', collected)
        self.selenium_logger.info('Ecommerce Demo App - %s - %s', datetime.now(),self.url)
