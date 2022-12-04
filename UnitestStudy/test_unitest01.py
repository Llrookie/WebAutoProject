import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCase(unittest.TestCase):
    def test_login_02(self):
        driver = webdriver.Chrome()
        driver.get('https://baidu.com')
        driver.find_element(By.ID,'kw').send_keys('你是个二傻子吗')
        time.sleep(3)

    def test_login_01(self):
        print('测试用例2')

