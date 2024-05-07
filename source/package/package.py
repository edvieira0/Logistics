class Package:
    def __init__(self, browser):
        self.browser = browser
        # self.package_id = package_id
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