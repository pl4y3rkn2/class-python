import unittest
from selenium import webdriver
from test_google import GooglePage

class GoogleTest(unittest.TestCase):

    @classmethod#Decoradores para correr en una sola instancia del navegador
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path= 'C:\webdriver\chromedriver.exe')

    def test_search(self):
        google = GooglePage(self.driver)
        google.open()
        google.search('Python')

        self.assertEqual('Python', google.keyword)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == '__main__':
    unittest.main()