import unittest
from selenium import webdriver

class Typos(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='C:/webdriver/chromedriver.exe')
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com/")
        driver.find_element('link text', 'Typos').click()

    def test_find_typo(self):
        driver = self.driver
        text_to_check = driver.find_element('css selector', '#content > div > p:nth-child(3)').text
        tries = 1
        correct_text = "Sometimes you'll see a typo, other times you won't."
        while text_to_check != correct_text:
            text_to_check = driver.find_element('css selector''#content > div > p:nth-child(3)').text
            tries += 1
            driver.refresh()
        print(f'It took {tries} tries to find the typo')

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity = 2)