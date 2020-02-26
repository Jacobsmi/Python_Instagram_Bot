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
        notNowButton = WebDriverWait(driver, 15).until(lambda d: d.find_element_by_xpath('//button[text()="Not Now"]'))
        notNowButton.click()
        self.action(driver)

        

    def action(self,driver):
        search = driver.find_element(By.XPATH, '//input[@placeholder="Search"]')
        search.send_keys("#posthardcore")
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(1)
        search.send_keys(Keys.ENTER) 
        done = input("Press enter when you are done")
        if(done == ""):
            driver.quit()