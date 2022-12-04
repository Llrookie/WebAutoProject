'''
  键盘操作：
    send_keys(Keys.BACK_SPACE):删除
    send_keys(Keys.ENTER):回车
    send_keys(Keys.SPACE):空格
    send_keys(Keys.TAB):Tab键
    send_keys(Keys.ESCAPE):ESC键
    send_keys(Keys.CONTROL,'a'):全选
    send_keys(Keys.CONTROL,'c'):复制
    send_keys(Keys.CONTROL,'v'):粘贴
    send_keys(Keys.CONTROL,'x'):剪贴

'''
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
# 百度seleniumm
driver.find_element(By.ID, 'kw').send_keys('seleniumm')
time.sleep(2)
driver.find_element(By.ID, 'kw').send_keys(Keys.ESCAPE)
# 删除多余的m
driver.find_element(By.ID, 'kw').send_keys(Keys.BACK_SPACE)
time.sleep(1)
# 再输入空格 教程,再次发送字符串，是拼接
driver.find_element(By.ID, 'kw').send_keys(' 教程')
time.sleep(1)
# ctrl+a,全选文本框内容
driver.find_element(By.ID, 'kw').send_keys(Keys.CONTROL, 'a')
time.sleep(1)
# ctrl+x,剪贴选择的内容
driver.find_element(By.ID, 'kw').send_keys(Keys.CONTROL, 'x')
time.sleep(1)
# ctrl+v,粘贴复制的内容
driver.find_element(By.ID, 'kw').send_keys(Keys.CONTROL, 'v')
time.sleep(1)
# 回车代替点击，完成搜索
driver.find_element(By.ID, 'kw').send_keys(Keys.ENTER)
time.sleep(1)
# 退出浏览器
driver.quit()
