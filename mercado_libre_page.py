from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MercadoLibrePage(object):

  def __init__(self, driver):
    self._driver = driver
    self._url = 'http://mercadolibre.com/'

  @property
  def is_loaded(self):
    WebDriverWait(self._driver, 10).until(
      EC.presence_of_element_located((By.CLASS_NAME, 'ml-site-list'))
      or EC.presence_of_element_located((By.NAME, 'as_word'))
    )
    return True

  @property
  def keyword(self):
    input_field = self._driver.find_element('name', 'as_word')
    return input_field.get_attribute('value')

  def open(self):
    self._driver.get(self._url)

  def type_search(self, keyword):
    input_field = self._driver.find_element('name', 'as_word')
    input_field.send_keys(keyword)

  def click_submit(self):
    input_field = self._driver.find_element('name', 'as_word')
    input_field.submit()

  def search(self, keyword):
    self.type_search(keyword)
    self.click_submit()

  def order_data(self, elements):
    obj = {}
    for element in elements:
      obj[element.text.lower()] = element
    return obj

  def get_contries(self):
    contries = self._driver.find_elements('class name','ml-site-link')
    return self.order_data(contries)

  def choise_contry(self, contry):
    contry_item = self.get_contries()[contry.lower()]
    contry_item.click()

  def get_filters(self):
    filters = WebDriverWait(self._driver, 10).until(EC.visibility_of_any_elements_located((By.CLASS_NAME, 'ui-search-filter-name')))
    return self.order_data(filters)

  def choise_filter(self, keyword):
    self.get_filters()[keyword.lower()].click()

  def get_orders(self):
    list_buttom = WebDriverWait(self._driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'andes-dropdown__trigger')))
    list_buttom.click()
    orders = self._driver.find_elements('class name', 'andes-list__item-primary')
    return self.order_data(orders)

  def choise_order_by(self, keyword):
    self.get_orders()[keyword.lower()].click()

  def get_top_5_elements_result(self):
    WebDriverWait(self._driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'ui-search-layout__item')))
    data = [[None, None]] * 5
    for i in range(5):
      data[i][0] = self._driver.find_element('xpath', f'//*[@id="root-app"]/div/div/section/ol/li[{i+1}]/div/div/div[2]/div[1]/a/h2').text
      data[i][1] = self._driver.find_element('xpath', f'//*[@id="root-app"]/div/div/section/ol/li[{i+1}]/div/div/div[2]/div[2]/div/div/span[1]/span[2]').text
    return data