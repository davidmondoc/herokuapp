from time import sleep
from pages.base_page import Base_page
from selenium.webdriver.common.by import By

class login_page( Base_page ):

    USER = (By.XPATH, f'//*[@id="username"]')
    PASSWORD = (By.XPATH, f'//*[@id="password"]')
    LOGIN_BTN = (By.TAG_NAME, 'button')


    def navigate_to_page(self):
        self.chrome.get("https://the-internet.herokuapp.com/login")

    def user_action(self):
        self.chrome.find_element(*self.USER).send_keys('tomsmith')

    def password_action(self):
        self.chrome.find_element(*self.PASSWORD).send_keys('SuperSecretPassword!')

    def login_action(self):
        self.chrome.find_element(*self.LOGIN_BTN).click()

    def user_login(self, user, password):
        self.user_action(user)
        self.password_action(password)
        self.login_action()

    def check_current_url(self):
        actual_url = self.chrome.current_url
        expected_url = 'https://the-internet.herokuapp.com/login'
        self.assertEqual ( actual_url , expected_url , "The url does not match" )