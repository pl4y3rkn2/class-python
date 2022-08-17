import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestingMercadolibre(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Chrome(executable_path = 'C:\webdriver\chromedriver.exe')
    driver = self.driver
    driver.get('https://www.mercadolibre.com')
    driver.maximize_window()

  def test_search_ps4(self):
    driver = self.driver

    country = driver.find_element('id', 'VE')
    country.click()

    search_field = driver.find_element('name', 'as_word')
    search_field.click()
    search_field.clear()
    search_field.send_keys('playstation 4')
    search_field.submit()

    location = driver.find_element('partial_Link_Text', 'Distrito Capital')
    location.click()
    condition = driver.find_element('partial_Link_Text', 'Nuevo')
    condition.click()
          
    order_menu = driver.find_element('xpath', '/html/body/main/div/div[2]/section/div[1]/div/div/div/div[2]/div/button/span')
    order_menu.click()
    higher_price = driver.find_element('xpath', '/html/body/main/div/div[2]/section/div[1]/div/div/div/div[2]/div/div/div/div/ul/li[3]/div/div/span')
    higher_price.click()

    articles = []
    prices = []

    for i in range(5):
      article_name = driver.find_element('xpath', f'/html/body/main/div/div[2]/section/ol/li[{i + 1}]/div/div/div[2]/div[1]/a/h2').text
      articles.append(article_name)
      article_price = driver.find_element('xpath', f'/html/body/main/div/div[2]/section/ol/li[{i + 1}]/div/div/div[2]/div[2]/div[1]/div/div/div/div/span[1]/span[2]/span[2]').text
      prices.append(article_price)

    print(articles)
    print(prices)

  #def tearDown(self):
  #  self.driver.close()

if __name__ == "__main__":
  unittest.main(verbosity=2)
