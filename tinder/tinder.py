from selenium import webdriver
from time import sleep
import chromedriver_binary
from secrets import address,password
class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
    def login(self):
        sleep(1)
        self.driver.get('https://tinder.com')
        sleep(4)

        # cookies = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/button')
        # cookies.click()
        sleep(4)
        fb_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[2]/div[2]/div/div/span/div[2]/button')
        fb_btn.click()

        #switch to login popup
        base_window= self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])
        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(address)
        pass_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pass_in.send_keys(password)
        login_btn = self.driver.find_element_by_xpath('//*[@id="loginbutton"]')
        login_btn.click()
        self.driver.find_element_by_xpath('//*[@id="u_0_4"]/div[2]/div[1]/div[1]/button').click()

        self.driver.switch_to_window(base_window)

        popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button/span')
        popup_1.click()

        popup_2 = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div/div[2]/button/svg/path')
        popup_2.click()


bot = TinderBot()
bot.login()