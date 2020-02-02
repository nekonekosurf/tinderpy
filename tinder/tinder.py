from selenium import webdriver
from time import sleep
import chromedriver_binary
class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()


    def login(self):
        self.driver.get('https://tinder.com')
        sleep(2)
        fb_btn = self.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[2]/div[2]/div/div/span/div[2]/button')
        fb_btn.click()

        #switch to login popup
        base_window= self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])
        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys('n*******@gmail.com')
        pass_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pass_in.send_keys('password')
        login_btn = self.driver.find_element_by_xpath('//*[@id="loginbutton"]')
        login_btn.click()