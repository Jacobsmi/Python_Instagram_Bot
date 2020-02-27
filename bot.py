import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Bot:
    def __init__(self, username, password):
        self.username = username
        self.password = password


    def getHashtags(self):
        all_Hashtags = []
        more_Hashtags = True
        print("Please enter a hashtag you wish to search for\nWhen you are done press enter twice.\n")
        while(more_Hashtags):
            hashtag = input("Enter your hashtag here:")
            if(hashtag == ""):
                more_Hashtags = False
                self.hashtags = all_Hashtags
            else:
                all_Hashtags.append(hashtag)
                more_Hashtags = True


    def login(self):
        driver = webdriver.Chrome('C:/bin/chromedriver')  #Argument that points to the Chrome Driver
        driver.get('https://www.instagram.com/accounts/login/');
        time.sleep(1) #Navigates to the link and waits so user can see what is happening
        username = driver.find_element_by_name('username')#Defines the username input field
        username.send_keys(self.username) #Enters the username 
        password = driver.find_element_by_name('password')#Defines the password input field
        password.send_keys(self.password)#Enters the password
        password.submit()#Submits the password field in order to finish the login process
        notNowButton = WebDriverWait(driver, 15).until(lambda a: a.find_element_by_xpath('//button[text()="Not Now"]'))
        notNowButton.click()
        self.action(driver)

        

    def action(self,driver):
        # Creates a for loop that allows the bot to search for all the hashtags given to it
        for hashtag in self.hashtags:
            # Redirects from whatever page it was on to the homepage
            driver.get('https://www.instagram.com/')
            # Finds the search bar by looking for the XPath 
            # Create an object search 
            search = driver.find_element_by_xpath('//input[@placeholder="Search"]')
            # React element so you must clear the text area
            search.clear()
            # Create a hashtag to search for from the user input
            search_text = "#" + hashtag
            # Type the desired hashtag into the search bar
            search.send_keys(search_text)
            # Creates the XPath string to find the correct button
            hashtag_xpath = '//*[text()="{}"]'.format(search_text)
            # Causes the driver to wait until the specified element is found
            # In this case the element being waited for is the hashtag button
            # Then we set the hashtag_button object to the button
            hashtag_button = WebDriverWait(driver, 15).until(lambda a: a.find_element_by_xpath(hashtag_xpath))
            # Then click the button to redirect to that page
            hashtag_button.click()
            time.sleep(5)

        done = input("Press enter when you are done")
        if(done == ""):
            driver.quit()
