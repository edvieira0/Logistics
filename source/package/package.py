class Package:
    def __init__(self, browser, package_id):
        self.browser = browser
        self.package_id = package_id
        self.export_data = True

    def get_json(self):
        """
        Função com o objetivo de varrer a página em busca de um json contendo informações.
        """
        import re
        import json

        page_content = self.browser.driver.page_source
        json_data = None

        if page_content:
            match = re.search(r'window\.__PRELOADED_STATE__\s*=\s*({.*?});', page_content, re.DOTALL)

            if match:
                json_data = match.group(1)

                if self.export_data == True:
                    #export json files to data/json_files
                    with open(f'data/json_files/{self.package_id}.json', 'w', encoding='utf-8') as json_file:
                        json_file.write(json_data)

        if json_data is not None:
            return json.loads(json_data)
        else:
            raise FileNotFoundError('JSON not Found.')

    def extract_infos(self, url):
        self.browser.driver.get(url)
        json_files = self.get_json()
        print(json_files)

    def change_status(self):
        ...

    def update_database(self):
        ...
    
    def login(self,user, password):
        def search_xpath_by_elements(xpath, extra_xpath=None):
            from selenium.webdriver.common.by import By
            from selenium.common.exceptions import NoSuchElementException

            try:
                element_xpath = self.browser.driver.find_elements(by=By.XPATH, value=xpath)
                if len(element_xpath) > 1:
                    # print(f'Mais de um elementos encontrados na página.')
                    for i in element_xpath:
                        # print(i.text)
                        return element_xpath
                elif len(element_xpath) == 1:
                    return element_xpath[0]
                else:
                    return None
            except NoSuchElementException:
                print(f'Erro ao encontrar xpath.')
                return None
        
        import time
        import os
        import sys
        self.browser.driver.get(url='https://envios.adminml.com/tools/home')

        button_select = search_xpath_by_elements(xpath='//div[@class="auth0-lock-social-button-text"]')
        if button_select[1] != None:
            button_select[1].click()
        else:
            print('Error Fatal, dei kill nos processos.')
            sys.exit()

        time.sleep(5)
        #Procura os campos e preenchem com informações.

        user_xpath = search_xpath_by_elements(xpath='//input[@name="username"]')
        if user_xpath != None:
            for i in user:
                user_xpath.send_keys(i)
                time.sleep(0.1)

        pass_xpath = search_xpath_by_elements(xpath='//input[@name="password"]')
        if pass_xpath != None:
            for i in password:
                pass_xpath.send_keys(i)
                time.sleep(0.1)

        submit_button = search_xpath_by_elements(xpath='//button[@type="submit"]')
        if submit_button != None:
            submit_button.click()
        else:
            print('erro ao clicar.')

        time.sleep(4)
        os.system("cls")