class Package:
    def __init__(self):
        pass

    def get_json(self, browser, url, id_json):
        
        import re
        import json

        browser.driver.get(f'{url}{id_json}')
        page_content = browser.driver.page_source

        if page_content:
            match = re.search(r'window\.__PRELOADED_STATE__\s*=\s*({.*?});', page_content, re.DOTALL)

            if match:
                json_data = match.group(1)

                #export json files to data/json_files
                with open(f'data/json_files/{id_json}.json', 'w', encoding='utf-8') as json_file:
                    json_file.write(json_data)
            return json.loads(json_data)
        else:
            print(f'Error, page content not found.')
            raise FileNotFoundError
    
    def get_info(self, get_json):
        if get_json:
            ...