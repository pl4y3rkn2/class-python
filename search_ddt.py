import csv, unittest
from ddt import ddt, data, unpack
from selenium import webdriver

def get_data(file_name):
    rows = []
    data_file= open(file_name, 'r')
    reader= csv.reader(data_file)
    next(reader, None)

    for row in reader:
        rows.append(row)

    return rows


@ddt
class SearchDDT(unittest.TestCase):
    def setUp(self):
        self.driver= webdriver.Chrome(executable_path= "c:\webdriver\chromedriver.exe")
        driver= self.driver
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com')
    @data(*get_data('testdata.csv'))
    @unpack
    def test_search_ddt(self, search_value, expected_count):
        driver= self.driver

        search_field= driver.find_element('name', 'q')
        search_field.clear()
        search_field.send_keys(search_value)
        search_field.submit()

        products = driver.find_elements('xpath', '//h2[@class= "product-name"]/a')
        expected_count = int(expected_count)
        if expected_count>0:
            self.assertEqual(expected_count, len(products))
        else:
            message= driver.find_elements('class name', 'note-msg')
            self.assertEqual('Your search returns no results.', message)
        print(f'Found {len(products)} products')
        
     
        
if __name__== '__main__':
    unittest.main(verbosity=2)