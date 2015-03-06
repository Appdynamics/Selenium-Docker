import sys
import os
import gc
import time
import random
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import UnexpectedAlertPresentException
from SeleniumScript import SeleniumScript


class PHPDemoApp(SeleniumScript): 

    def request(self):
        
        try:
            _timeout = 60
            pageWait = 2
            
            self.selenium_logger.info('PHP Demo : %s', self.url)

            r1 = random.randint(1,4)

            for i in range(r1):

                r2 = random.randint(1,4)

                if r2 == 1:
                    product_name = "A Foo Bar"
                elif r2 == 2:
                    product_name = "A Foo Bar2"
                elif r2 == 3:
                    product_name = "Big Tank"
                elif r2 == 4:
                    product_name = "Product 1"

                w = WebDriverWait(self.driver, _timeout)
                w.until(lambda driver: self.driver.find_element_by_link_text(product_name))
                product = self.driver.find_element_by_link_text(product_name)
                self.selenium_logger.debug('product = %s', product_name)
                product.click()
                time.sleep(pageWait)

                w = WebDriverWait(self.driver, _timeout)
                w.until(lambda driver: self.driver.find_elements_by_tag_name("input"))
                addtocart = self.driver.find_elements_by_tag_name("input")
                self.selenium_logger.debug('add to cart')
                addtocart[3].click()
                time.sleep(pageWait)
                
                w = WebDriverWait(self.driver, _timeout)
                w.until(lambda driver: self.driver.find_element_by_link_text("Home"))
                home = self.driver.find_element_by_link_text("Home")
                self.selenium_logger.debug('home')
                home.click()
                time.sleep(pageWait)

            w = WebDriverWait(self.driver, _timeout)
            w.until(lambda driver: self.driver.find_element_by_link_text("View Cart"))
            viewcart = self.driver.find_element_by_link_text("View Cart")
            self.selenium_logger.debug('view cart')
            viewcart.click()
            time.sleep(pageWait)

            w = WebDriverWait(self.driver, _timeout)
            w.until(lambda driver: self.driver.find_element_by_link_text("Checkout"))
            checkout = self.driver.find_element_by_link_text("Checkout")
            self.selenium_logger.debug('checkout')
            checkout.click()
            time.sleep(pageWait)

            w = WebDriverWait(self.driver, _timeout)
            w.until(lambda driver: self.driver.find_element_by_link_text("Search"))
            search = self.driver.find_element_by_link_text("Search")
            self.selenium_logger.debug('search')
            search.click()
            time.sleep(pageWait)

            w = WebDriverWait(self.driver, _timeout)
            w.until(lambda driver: self.driver.find_element_by_id("home"))
            home = self.driver.find_element_by_id("home")
            self.selenium_logger.debug('home')
            home.click()
            time.sleep(pageWait)

            # Performing garbage collection
            collected=gc.collect()
            self.selenium_logger.debug('Garbage collector: collected %d objects.', (collected))
            self.selenium_logger.info('PHP Demo - %s - %s', datetime.now(),self.url)
            
        except UnexpectedAlertPresentException as uape: 
            self.selenium_logger.debug('PHP Demo - UnexpectedAlertPresentException: {0}'.format(uape))
            alert = self.driver.switch_to_alert()
            alert.dismiss()
            self.selenium_logger.debug('PHP Demo - %s - %s', datetime.now(),self.url)
            w = WebDriverWait(self.driver, _timeout)
            w.until(lambda driver: self.driver.find_element_by_id("home"))
            home = self.driver.find_element_by_id("home")
            self.selenium_logger.debug('home')
            home.click()
            time.sleep(pageWait)
        except IndexError as ie: 
            self.selenium_logger.error('Index Error')
            self.selenium_logger.error('Current URL = %s', self.driver.current_url)
            self.selenium_logger.error('Page Source:')
            self.selenium_logger.error(self.driver.page_source)

