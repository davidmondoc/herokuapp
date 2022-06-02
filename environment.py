from browser import Browser
from pages.home_page import *
from pages.login_page import *
from pages.secure_page import *

def before_all(context):
    context.browser = Browser()
    context.home = home_page()
    context.login = login_page()
    context.secure = secure_page()

def after_all(context):
    context.browser.close()