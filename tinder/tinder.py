from selenium import webdriver
from time import sleep
import chromedriver_binary
import secrets

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
    def login(self):
        sleep(1)
        self.driver.get('https://tinder.com')
        sleep(1)
        address=secrets.address_()
        password=secrets.password_()
        # cookies = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/button')
        # cookies.click()
        sleep(2)

        while True:
            try:
                # fb_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button/span')
                fb_btn = self.driver.find_element_by_xpath('//*[@id="t-1801132545"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button/span')


                fb_btn.click()
                break
            except Exception:
                sleep(2)
                print("cant login google0")
        sleep(4)
        while True:
            try:
                # google=self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[1]/div/button/span[2]')
                google=self.driver.find_element_by_xpath('//*[@id="t--239073259"]/div/div/div[1]/div/div[3]/span/div[1]/div/button')


                google.click()
                break
            except Exception:
                sleep(2)
                print("cant login google")

        sleep(1)
        # switch to login popup
        base_window = self.driver.window_handles[0]
        sleep(2)
        while True:
            try:
                self.driver.switch_to_window(self.driver.window_handles[1])
                break
            except Exception:
                sleep(2)
                print("cannt")
                google = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[1]/div/button/span[2]')
                google.click()

        email_in = self.driver.find_element_by_xpath('//*[@id="identifierId"]')
        email_in.send_keys(address)
        next = self.driver.find_element_by_xpath('// *[ @ id = "identifierNext"] / div / button')
        next.click()
        sleep(4)
        pass_in = self.driver.find_element_by_xpath('// *[ @ id = "password"] / div[1] / div / div[1] / input')
        pass_in.send_keys(password)
        next = self.driver.find_element_by_xpath('// *[ @ id = "passwordNext"] / div / button / div[2]')
        next.click()
        self.driver.switch_to_window(base_window)
        sleep(8)
        while True :
            try:
                # geo=self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]/span')
                geo=self.driver.find_element_by_xpath('//*[@id="t--239073259"]/div/div/div/div/div[3]/button[1]')

                geo.click()
                break
            except Exception:
                print("!error!")
                pass
        sleep(4)
        # self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]/span').click()
        self.driver.find_element_by_xpath('//*[@id="t--239073259"]/div/div/div/div/div[3]/button[1]').click()

    def like(self):
        # like=self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button/span')
        like=self.driver.find_element_by_xpath('//*[@id="t-1801132545"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button')
        like.click()


    def dislike(self):
        dislike=self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button/span')
        dislike.click()

    def close_popup_superlike(self):
        self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/button[2]/span').click()

    def close_popup_liked(self):
        self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div[3]/button[2]/span').click()

    def close_popup_addHome(self):
        self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]/span').click()

    def matched(self):
        sentence=' '
        text_area=self.driver.find_element_by_xpath('//*[@id="chat-text-area"]')
        text_area.send_keys(sentence)
        self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/div[3]/form/button/span').click()

        # self.driver.find_element_by_xpath('// *[ @ id = "t-1801132545"] / div / div[1] / div / main / div[1] / div / div / div / div / header / div / div[2] / div[2] / button / span').click()




    def auto_swipe(self):
        while True:
            sleep(1)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup_superlike()
                except Exception:
                    try:
                        self.close_popup_liked()
                    except Exception:
                        try:
                            self.close_popup_addHome()
                        except Exception:
                            try:
                                self.matched()
                                print("match")
                            except Exception:
                                print("error has occurered")

def main():
    bot = TinderBot()
    bot.login()
    bot.auto_swipe()



if __name__ == '__main__':
    main()

#pip install chromedriver-binary==76.0.3809.132
