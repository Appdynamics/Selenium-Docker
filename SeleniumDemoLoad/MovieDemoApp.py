import sys
import gc
import time
import random
from  datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from SeleniumScript import SeleniumScript

class MovieDemoApp(SeleniumScript): 

    def request(self):
        
        movies = ['99407652-9484-4eb5-890f-8c8ad045e593','b40fa3f6-5399-4d2e-ad74-dadb1a5d0d71','8437b0ba-fac9-4c74-8a30-21d263cf2728','7eed60f5-9713-45b8-aa76-a990bc69ce10','97ffc682-c982-446e-9d7e-5ab54aec2ce5','c3971cdd-acc2-43ba-af17-00aa8aee9d3d','b4d53caf-71cb-49ba-909d-71b8671064a0','6420f70e-e71e-4380-90f3-6dd46536f651','633fb347-5395-4913-bd42-97fe81a82596','f229e99c-31b0-40a0-87cd-d6646461273c']
        slowfrequency=10
        checkoutfrequency=5
        _timeout=25
            
        self.selenium_logger.info('Movie Demo App:  %s', self.url)
        
        # request the home page
        self.driver.get(self.url)
        
        self.selenium_logger.debug(self.driver.title)
        w = WebDriverWait(self.driver, _timeout)
        w.until(lambda driver: self.driver.find_element_by_link_text("Login"))
        login = self.driver.find_element_by_link_text("Login")
        
        login.click()
        
        #locate the username text box and submit button
        w = WebDriverWait(self.driver, _timeout)
        w.until(lambda driver: self.driver.find_element_by_name("username"))
        usernameTextBox = self.driver.find_element_by_name("username")
        submit = self.driver.find_element_by_name("buttonLogin")
        
        #Generating random number to decide whether to login as John Doe and cause an error
        r = random.randint(1,int(slowfrequency))
        
        if r == 1:
            self.selenium_logger.debug('John Doe Login')
            usernameTextBox.send_keys("John Doe")
            submit.click()
        else:
        
            login = random.randint(1, 10)
        
            if login == 1:
                self.selenium_logger.debug('Peter Parket Login')
                usernameTextBox.send_keys("Peter Parker")
                submit.click()
            else:
                self.selenium_logger.debug('Alex Fedotyev Login')
                usernameTextBox.send_keys("Alex Fedotyev")
                submit.click()
        
            movieIndex = random.randint(0,len(movies)-1)
        
            r = random.randint(1,int(checkoutfrequency))
            if r == 1:
        
                self.selenium_logger.debug('Normal Checkout')
                w = WebDriverWait(self.driver, _timeout)
                w.until(lambda driver: self.driver.find_element_by_name("movie"))
                self.selenium_logger.debug('getting movie')
                movieTextBox = self.driver.find_element_by_name("movie")
                self.selenium_logger.debug('getting count')
                countTextBox = self.driver.find_element_by_name("count")
                self.selenium_logger.debug('movie and count elements found')
        
                r2 = random.randint(1,10)
        
                if r2 == 1:
                    self.selenium_logger.debug('Slow Checkout')
                    movieTextBox.send_keys("795c3a05-c672-442c-993a-38103cb004d5")
                    self.selenium_logger.debug('1 copy')
                    countTextBox.send_keys("1")
                else:
                    self.selenium_logger.debug('Checkout')
                    movieTextBox.send_keys(movies[movieIndex])
                    self.selenium_logger.debug('5 copies')
                    countTextBox.send_keys("5")
        
                self.selenium_logger.debug('AddToCart')
                # Add to the cart
                w = WebDriverWait(self.driver, _timeout)
                w.until(lambda driver: self.driver.find_element_by_name("buttonCartAdd"))
                addToCartButton = self.driver.find_element_by_name("buttonCartAdd")
                addToCartButton.click()
        
                self.selenium_logger.debug('Checkout')
                # click the checkout link
                w = WebDriverWait(self.driver, _timeout)
                w.until(lambda driver: self.driver.find_element_by_link_text("Checkout"))
                checkoutLink = self.driver.find_element_by_link_text("Checkout")
                checkoutLink.click()
        
            else:
        
                #locate the Movies link and click it
                self.selenium_logger.debug('Search Request')
                w = WebDriverWait(self.driver, _timeout)
                w.until(lambda driver: self.driver.find_element_by_link_text('Movies'))
                movieLink = self.driver.find_element_by_link_text('Movies')
                movieLink.click()
                self.selenium_logger.debug('Clicked Movies Link')
        
                w = WebDriverWait(self.driver, _timeout)
                w.until(lambda driver: self.driver.find_elements_by_tag_name("input"))
                textSearch = self.driver.find_element_by_name("textSearch")
                buttonSearch = self.driver.find_element_by_name("buttonSearch") 
                textReviews = self.driver.find_element_by_name("textReviews")
                buttonReviews = self.driver.find_element_by_name("buttonReviews")
                textDetails = self.driver.find_element_by_name("textDetails")
                buttonDetails = self.driver.find_element_by_name("buttonDetails")

                r = random.randint(1,4)
                r2 = random.randint(1,10)
        
                if r == 1:
        
                    if r2 == 1:
                        self.selenium_logger.debug('Slow Search')
                        textSearch.send_keys("795c3a05-c672-442c-993a-38103cb004d5")
                    else:
                        self.selenium_logger.debug('Search')
                        textSearch.send_keys(movies[movieIndex])
                    buttonSearch.click()

                elif r == 2:
                    self.selenium_logger.debug('Reviews')
                    textReviews.send_keys(movies[movieIndex])
                    buttonReviews.click()
                else:
                    r = random.randint(1,int(slowfrequency))
                    if r == 1:
                        self.selenium_logger.debug('Slow Details')
                        textDetails.send_keys("795c3a05-c672-442c-993a-38103cb004d5")
                    else:
                        self.selenium_logger.debug('Details')

                        textDetails.send_keys(movies[movieIndex])

                    buttonDetails.click()
            self.selenium_logger.debug('Logout')
            #locate the Logout link and click it
            w = WebDriverWait(self.driver, _timeout)
            w.until(lambda driver: self.driver.find_element_by_link_text('Logout'))
            logoutLink = self.driver.find_element_by_link_text('Logout')
            logoutLink.click()
        time.sleep(2)
        
        #Performing garbage collection
        collected=gc.collect()
        self.selenium_logger.debug('Garbage collector: collected %d objects.', (collected))
        self.selenium_logger.info('Movie Ticket - %s - %s', datetime.now(), self.url)

                                                                                                                                           
