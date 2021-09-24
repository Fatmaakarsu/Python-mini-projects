from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# class Instagram():
#     def __init__(self,userName,password):
#         self.browser = webdriver.Chrome()
#         self.username = userName
#         self.password = password

#     def sign(self):
#         self.browser.get("https://www.github.com")
#         time.sleep(3)

#         userNameInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
#         passwordInput = self.browser.find_elements_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")

#         userNameInput.send_keys(self.userName)
#         passwordInput.send_keys(self.password)
#         passwordInput.send_keys(Keys.ENTER)

    

# insta = Instagram("helll","dnjkjcd")

driver = webdriver.Chrome()
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(2)

# username
driver.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input").send_keys("username")
# password
driver.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input").send_keys("password")
time.sleep(1)
# sign
driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]").click()



