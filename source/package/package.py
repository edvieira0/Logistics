class Package:
    def __init__(self, package_id):
        self.package_id = package_id
        self.export_data = True

    def get_json(self, browser, url):
        
        import re
        import json

        browser.driver.get(f'{url}{self.package_id}')
        page_content = browser.driver.page_source

        if page_content:
            match = re.search(r'window\.__PRELOADED_STATE__\s*=\s*({.*?});', page_content, re.DOTALL)

            if match:
                json_data = match.group(1)

                if self.export_data == True:
                    #export json files to data/json_files
                    with open(f'data/json_files/{self.package_id}.json', 'w', encoding='utf-8') as json_file:
                        json_file.write(json_data)

            return json.loads(json_data)
        else:
            print(f'Error, page content not found.')
            raise FileNotFoundError

    def change_status(self):
        ...

    def get_info(self):
        ...
    
    def update_database(self):
        ...