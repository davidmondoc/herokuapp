from time import sleep
from pages.base_page import Base_page
from selenium.webdriver.common.by import By

class home_page( Base_page ):
    FORM_AUTH = (By.LINK_TEXT , 'Form Authentication')
    BASIC_AUTH = (By.LINK_TEXT , 'Basic Auth')
    DIGEST_AUTH = (By.LINK_TEXT , 'Digest Authentication')
    FILE_DOWNLOAD = (By.LINK_TEXT , 'File Download')
    FILE_UPLOAD = (By.LINK_TEXT, 'File Upload')

    def navigate_to_page(self):
        self.chrome.get("https://the-internet.herokuapp.com/")

    def click_form(self):
        self.chrome.find_element(*self.FORM_AUTH).click()

    def click_basic(self):
        self.chrome.find_element ( *self.BASIC_AUTH ).click ( )

    def click_digest(self):
        self.chrome.find_element ( *self.DIGEST_AUTH ).click ( )

    def click_download(self):
        self.chrome.find_element ( *self.FILE_DOWNLOAD ).click ( )

    def click_upload(self):
        self.chrome.find_element ( *self.FILE_UPLOAD ).click ( )

    def check_current_url(self):
        actual_url = self.chrome.current_url
        expected_url = 'https://the-internet.herokuapp.com/'
        self.assertEqual ( actual_url , expected_url , "The url does not match" )