from source.browser.browser import Browser
from login import login
from scts import user_logistic, password_logistic

browser_instance = Browser('chrome')

login(browser_instance, user_logistic, password_logistic)