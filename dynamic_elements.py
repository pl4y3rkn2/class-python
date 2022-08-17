import unittest
from selenium import webdriver
from time import  sleep

class DynamicElement(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = 'C:\webdriver\chromedriver')
        driver = self.driver
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element('link text','Disappearing Elements').click()

    def test(self):
        driver = self.driver
        intentos = 1
        #Capturo los elementos de la lista
        elements = driver.find_elements('tag name', 'li')

        while len(elements) < 5:
            #Si los elementos que encontré son menores a 5 recargo la pagina y vuelvo a "contar" los elementos de la lista
            print('Elementos en la lista', len(elements))
            driver.refresh()
            elements = driver.find_elements('tag name', 'li')
            #Sumo otro intento
            intentos += 1
            #Espero 1 segundo para que poder ver cuántas veces ha recargado
            sleep(1)

        print(f'Nos tomó {intentos} intentos para capturar a Gallery')


    def tearDown(self):
        self.driver.quit()
        
if __name__ == '__main__':
    unittest.main(verbosity=2)