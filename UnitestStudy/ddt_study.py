import time
import unittest

from ddt import ddt, data, unpack
from selenium import webdriver
from selenium.webdriver.common.by import By

from UnitestStudy.excelRead import excel_read


@ddt
class ddt_study(unittest.TestCase):

    @data(*excel_read().read_data())
    @unpack
    def test_login_QQ(self, index, username, pwd):
        print(index, username, pwd)

        driver = webdriver.Chrome()
        driver.get('https://mail.qq.com/')
        driver.switch_to.frame('login_frame')
        driver.find_element(By.ID, 'u').send_keys(username)
        driver.find_element(By.ID, 'p').send_keys(pwd)
        driver.find_element(By.ID, 'login_button').click()
        time.sleep(3)
        driver.quit()


if __name__ == '__main__':
    unittest.main()
