import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException #sirve como excepción para los assertions cuando queremos #validar la presencia de un elemento
from selenium.webdriver.common.by import By #ayuda a llamar a las excepciones que queremos validar

class AssertionsTest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = 'C:\webdriver\chromedriver.exe')
		driver = self.driver
		driver.implicitly_wait(5)
		driver.maximize_window()
		driver.get("http://demo.onestepcheckout.com/")

	def test_search_field(self):
		self.assertTrue(self.is_element_present(By.NAME, 'q'))

	def test_language_option(self):
		self.assertTrue(self.is_element_present(By.ID, 'select-language'))

	def tearDown(self):
		self.driver.quit()

	def	is_element_present(self, how, what):
		try:  
			self.driver.find_element(by = how, value = what) 
		except NoSuchElementException as variable:
			return False
		return True
        
if __name__ == '__main__':
    unittest.main(verbosity = 2)