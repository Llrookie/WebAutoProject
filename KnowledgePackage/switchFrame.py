import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://mail.qq.com/')

# switch.to.frame('frame名称')，进入对应frame框架
driver.switch_to.frame('login_frame')

# driver.switch_to.default_content()，从一个框架进入另一个框架，需要先退出这个，再进入

driver.find_element(By.ID, 'u').send_keys('******@qq.com')
driver.find_element(By.ID, 'p').send_keys('******')
driver.find_element(By.ID, 'login_button').click()

time.sleep(3)

"""
在浏览器当中，如果在页面进行了某个操作，结果浏览器打开了另外一个新窗口(tab)。
如果要操作新窗口当中的，页面元素，就需要窗口切换。
"""