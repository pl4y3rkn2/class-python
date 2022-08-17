import unittest
from selenium import webdriver

class SearchTests(unittest.TestCase):
    
    @classmethod 
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path = "C:\webdriver\chromedriver.exe")
        driver = cls.driver
        driver.get('http://demo-store.seleniumacademy.com')
        driver.maximize_window()
        driver.implicitly_wait(5)

    def test_search_test_field(self):
        search_field = self.driver.find_element("id", "search")

    def test_search_test_field_by_name(self):
        search_field = self.driver.find_element("name", "q")

    def test_search_test_field_class_name(self):
        search_field = self.driver.find_element("class name", "input-text")

    def test_search_button_enable(self):
        button = self.driver.find_element("class name", "button")

    def test_count_of_promo_banner_images(self):
        banner_list = self.driver.find_element("class name", "promos")
        banners = banner_list.find_elements("tag name", 'img')
        self.assertEqual(3, len(banners))

    def test_vip_promo(self):
        vip_promo = self.driver.find_elements('xpath', '//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[4]/a/img')

    def test_shopping_cart(self):
        shopping_cart_icon = self.driver.find_element("css selector", "div.header-minicart span.icon")
        
    def test_search_tee(self):
        driver = self.driver
        search_field = driver.find_element("name", "q")
        search_field.clear()

        search_field.send_keys("tee")
        search_field.submit()

    def test_search_salt_shaker(self):
        driver = self.driver
        search_field = driver.find_element("name", "q")
        search_field.clear()

        search_field.send_keys("salt shaker")
        search_field.submit()

        products = driver.find_elements("xpath", '/html/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a')
        self.assertEqual(1, len(products))

    @classmethod 
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2)