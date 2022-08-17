import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #Esperas explicitas

class DynamicControls(unittest.TestCase):
    #Prepara entorno de la prueba. 
    def setUp(self):
        self.driver = webdriver.Chrome('C:\webdriver\chromedriver')
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com/")
        driver.find_element('link text', 'Dynamic Controls').click()



    #Casos de prueba
    def test_dynamic_controls(self):
        driver = self.driver
        checkbox = driver.find_element('css selector', '#checkbox > input[type=checkbox]')
        checkbox.click()

        remove_add = driver.find_element('css selector', '#checkbox-example > button')
        remove_add.click()
    
        #Webdriver wait (driver, espera). hasta que (EC.el elemento sea clickable(tupla)) tupla (por selector CSS, "Selector")
        WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkbox > input[type=checkbox]")))
        remove_add.click()

        enable_disable_button = driver.find_element('css selector', '#input-example > button')
        enable_disable_button.click()

        WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-example > button")))
        
        text_area = driver.find_element('css selector', '#input-example > input[type=text]')
        text_area.send_keys('Platzi')

        enable_disable_button.click()

    #Finalizar
    def tearDow(self):
        self.driver.quit() #Revisar con close


if __name__ == "__main__":
    unittest.main(verbosity=2)