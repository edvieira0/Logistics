class Package:
    def __init__(self):
        pass

    def get_json(self, browser, id_json):
        import re

        browser.get(self.management_url)
        page_content = browser.driver.page_source        

        if page_content:
            match = re.search(r'window\.__PRELOADED_STATE__\s*=\s*({.*?});', page_content, re.DOTALL)

            if match:
                json_data = match.group(1)

                #export json files to data/json_files
                with open(f'data/json_files/{id_json}.json', 'w', encoding='utf-8') as json_file:
                    json_file.write(json_data)