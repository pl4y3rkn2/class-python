import unittest
from selenium import webdriver
from time import sleep

class Tables(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='C:/webdriver/chromedriver.exe')
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com/")
        driver.find_element('link text', 'Sortable Data Tables').click()

    def test_sorf_tables(self):
        driver = self.driver

        table_data = [[{'Last Name': 'Smith', 'First Name': 'John', 'Email': 'jsmith@gmail.com', 'Due': '$50.00', 'Web Site': 'http://www.jsmith.com'}, {'Last Name': 'Bach', 'First Name': 'Frank', 'Email': 'fbach@yahoo.com', 'Due': '$51.00', 'Web Site': 'http://www.frank.com'}, {'Last Name': 'Doe', 'First Name': 'Jason', 'Email': 'jdoe@hotmail.com', 'Due': '$100.00', 'Web Site': 'http://www.jdoe.com'}, {'Last Name': 'Conway', 'First Name': 'Tim', 'Email': 'tconway@earthlink.net', 'Due': '$50.00', 'Web Site': 'http://www.timconway.com'}] for i in range(5)]
        print(table_data)

        for i in range(1, 5):
            header = driver.find_element('xpath', f'/html/body/div[2]/div/div/table[1]/thead/tr/th[{i + 1}]/span')
            table_data[i].append(header.text)

            for j in range(1, 4):
                row_data = driver.find_element('xpath', f'/html/body/div[2]/div/div/table[1]/tbody/tr[{j + 1}]/td[1]')
                table_data[i].append(row_data.text)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity = 2)