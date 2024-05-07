from source.browser.browser import Browser
from login import login
from scts import user_logistic, password_logistic
from source.package import package

# browser_instance = Browser('chrome')

# login(browser_instance, user_logistic, password_logistic)

instance_teste = package.Package(Browser('chrome'))

instance_teste.extract_infos('https://www.youtube.com/')