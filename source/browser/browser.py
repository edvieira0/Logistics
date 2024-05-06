class Browser:
    def __init__(self, browser='firefox'):
        from selenium import webdriver
        from selenium.webdriver.firefox.options import Options as FirefoxOptions
        from selenium.webdriver.chrome.options import Options as ChromeOptions
        import os

        script_dir = os.path.dirname(os.path.abspath(__file__))

        download_path = os.path.join(script_dir, '..', '..', 'data', 'Downloads')
        download_path = os.path.abspath(download_path)

        if browser == 'firefox':
            firefox_options = FirefoxOptions()
            firefox_options.set_preference("browser.download.folderList", 2)
            firefox_options.set_preference("browser.download.dir", download_path)
            firefox_options.set_preference("browser.download.manager.showWhenStarting", False)
            firefox_options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
            self.driver = webdriver.Firefox(options=firefox_options)
        elif browser == 'chrome':
            chrome_options = ChromeOptions()
            chrome_prefs = {"download.default_directory": download_path}
            chrome_options.add_experimental_option("prefs", chrome_prefs)
            self.driver = webdriver.Chrome(options=chrome_options)
        else:
            raise ValueError("Tipo de navegador não suportado.")