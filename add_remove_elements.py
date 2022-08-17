import unittest
from selenium import webdriver
from time import sleep

class AddRemoveElements_Reto(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome(executable_path = 'C:\webdriver\chromedriver')
        driver = self.driver
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element('link text', 'Add/Remove Elements').click()

    
    def test_add_remove(self):
        driver = self.driver

        elements_added = int(input('Cuantos elementos desea agregar?: '))

        add_button = driver.find_element('xpath', '//*[@id="content"]/div/button')

        sleep(3)

        for i in range(elements_added):
            add_button.click()

        elements_removed = int(input("cuantos elementos quiere eliminar? "))

        for i  in range(elements_removed):
            try:
                delete_button = driver.find_element('xpath', '/html/body/div[2]/div/div/div/button')
                delete_button.click()
            except:
                print("Tu estas tratando de eliminar mas datos de los que existen")
                break

        total_elements = elements_added - elements_removed

        if total_elements == 1:

            print(f'Removiste {elements_removed} elementos, queda {total_elements} elemento')

        elif total_elements > 1 or total_elements < 1:
            
            print(f'Removiste {elements_removed}, quedan {total_elements} elementos')  

        sleep(3)                    
        
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity = 2)