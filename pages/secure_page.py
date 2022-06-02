from pages.base_page import Base_page
from selenium.webdriver.common.by import By

class secure_page(Base_page):
    MESSAGE=(By.XPATH, f'//*[@class="flash success"]' )
    LOGOUT_BTN=(By.LINK_TEXT, 'Logout')