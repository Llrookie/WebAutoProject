import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://baidu.com')
driver.maximize_window()
time.sleep(3)

# 控制鼠标悬浮到“设置”按钮上
setbutton = driver.find_element(By.ID, 's-usersetting-top')

# 将对“设置”按钮的操作行为封装到ActionChains，到这一步，鼠标对象已经知道要干啥了，还没开始
ActionChains(driver).move_to_element(setbutton).perform()

time.sleep(5)
driver.quit()
