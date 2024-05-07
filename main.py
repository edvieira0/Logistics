from source.browser.browser import Browser

browser_instance = Browser('firefox')

browser_instance.driver.get('https://www.google.com/')