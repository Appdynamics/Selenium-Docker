import sys
import gc
import time
import random
from urllib2 import URLError
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from SeleniumScript import SeleniumScript

class MovieDemoApp(SeleniumScript): 

    def request(self):
        
        movies = ['99407652-9484-4eb5-890f-8c8ad045e593','b40fa3f6-5399-4d2e-ad74-dadb1a5d0d71','8437b0ba-fac9-4c74-8a30-21d263cf2728','7eed60f5-9713-45b8-aa76-a990bc69ce10','97ffc682-c982-446e-9d7e-5ab54aec2ce5','c3971cdd-acc2-43ba-af17-00aa8aee9d3d','b4d53caf-71cb-49ba-909d-71b8671064a0','6420f70e-e71e-4380-90f3-6dd46536f651','633fb347-5395-4913-bd42-97fe81a82596','f229e99c-31b0-40a0-87cd-d6646461273c']
        slowfrequency=10
        checkoutfrequency=5
        _timeout=25
        
        print """Movie Demo App:  %s""" % (self.url)
        
        # request the home page
        self.driver.get(self.url)
        
        #print self.driver.title
        w = WebDriverWait(self.driver, _timeout)
        w.until(lambda driver: self.driver.find_element_by_link_text("Login"))
        login = self.driver.find_element_by_link_text("Login")
        
        login.click()
        
        #locate the username text box and submit button
        w = WebDriverWait(self.driver, _timeout)
        w.until(lambda driver: self.driver.find_element_by_name("username"))
        usernameTextBox = self.driver.find_element_by_name("username")
        submit = self.driver.find_elements_by_tag_name("input")
        #print "submit.parent = %s" % submit[2]
        
        #Generating random number to decide whether to login as John Doe and cause an error
        r = random.randint(1,int(slowfrequency))
        
        if r == 1:
            #print "John Doe Login"
            usernameTextBox.send_keys("John Doe")
            submit[3].click()
        else:
        
            login = random.randint(1, 10)
        
            if login == 1:
                #print "Peter Parket Login"
                usernameTextBox.send_keys("Peter Parker")
                submit[3].click()
            else:
                #print "Alex Fedotyev Login"
                usernameTextBox.send_keys("Alex Fedotyev")
                submit[3].click()
        
            movieIndex = random.randint(0,len(movies)-1)
        
            r = random.randint(1,int(checkoutfrequency))
            if r == 1:
        
                #print "Normal Checkout"
                #w = WebDriverWait(self.driver, _timeout)
                #w.until(lambda driver: self.driver.find_element_by_name("movie"))
                #print "getting movie"
                movieTextBox = self.driver.find_element_by_name("movie")
                #print "getting count"
                countTextBox = self.driver.find_element_by_name("count")
                #print "movie and count elements found"
        
                r2 = random.randint(1,10)
        
                if r2 == 1:
                    #print "Slow Checkout"
                    movieTextBox.send_keys("795c3a05-c672-442c-993a-38103cb004d5")
                    #print "1 copy"
                    countTextBox.send_keys("1")
                else:
                    #print "Checkout"
                    movieTextBox.send_keys(movies[movieIndex])
                    #print "5 copies"
                    countTextBox.send_keys("5")
        
                #print "AddToCart"
                # Add to the cart
                w = WebDriverWait(self.driver, _timeout)
                w.until(lambda driver: self.driver.find_elements_by_tag_name("input"))
                addToCartButton = self.driver.find_elements_by_tag_name("input")
                addToCartButton[2].click()
        
                #print "Checkout"
                # click the checkout link
                w = WebDriverWait(self.driver, _timeout)
                w.until(lambda driver: self.driver.find_element_by_link_text("Checkout"))
                checkoutLink = self.driver.find_element_by_link_text("Checkout")
                checkoutLink.click()
        
            else:
        
                #locate the Movies link and click it
                #print "Search Request"
                w = WebDriverWait(self.driver, _timeout)
                w.until(lambda driver: self.driver.find_element_by_link_text('Movies'))
                movieLink = self.driver.find_element_by_link_text('Movies')
                movieLink.click()
                #print "Clicked Movies Link" 
        
                w = WebDriverWait(self.driver, _timeout)
                w.until(lambda driver: self.driver.find_elements_by_tag_name("input"))
                search = self.driver.find_elements_by_tag_name("input")
        
                r = random.randint(1,4)
                r2 = random.randint(1,10)
        
                if r == 1:
        
                    if r2 == 1:
                        #print "Slow Search"
                        search[0].send_keys("795c3a05-c672-442c-993a-38103cb004d5")
                    else:
                        #print "Search"
                        search[0].send_keys(movies[movieIndex])
        
                        search[1].click()
                elif r == 2:
                    #print "Reviews"
                    search[2].send_keys(movies[movieIndex])
                    search[3].click()
                else:
                    r = random.randint(1,int(slowfrequency))
                    if r == 1:
                        #print "Slow Details"
                        search[4].send_keys("795c3a05-c672-442c-993a-38103cb004d5")
                    else:
                        #print "Details"
                        search[4].send_keys(movies[movieIndex])
                    search[5].click()
            #print "Logout"
            #locate the Logout link and click it
            w = WebDriverWait(self.driver, _timeout)
            w.until(lambda driver: self.driver.find_element_by_link_text('Logout'))
            logoutLink = self.driver.find_element_by_link_text('Logout')
            logoutLink.click()
        time.sleep(2)
        
        #Performing garbage collection
        collected=gc.collect()
        #print "Garbage collector: collected %d objects." % (collected)
        print "Movie Ticket - %s - %s" % (datetime.now(), self.url)
