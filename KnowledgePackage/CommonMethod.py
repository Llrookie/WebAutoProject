'''
 常用方法：
    clear():清除文本
    send_keys():模拟键盘输入
    click():点击元素
    current_url:返回当前页面的url地址，可用于断言
    title:获取当前页面的title
    Text():获取页面显示的文本(提示框、警告框)
    get_attribute(name):获取属性值，
    is_displayed():判断该属性是否用户可见
    is_enabled():判断该属性是否可用
    current_window_handle：获取当前页面的句柄(handler)
    window_handles：获取所有句柄
    switch_to_window(handler name):设置driver绑定的句柄
'''
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# 打开页面
driver.get("https://www.baidu.com")

# 获取文本并打印
textvalue = driver.find_element(By.ID, 'su').text
print(textvalue)

# 获取属性并打印
value1 = driver.find_element(By.ID, 'kw').get_attribute('name')
print(value1)  # wd

# 判断该属性是否可见
boo = driver.find_element(By.ID, 'su').is_displayed()
print(boo)

# 判断该属性是否可用
boo1 = driver.find_element(By.ID, 'su').is_enabled()
print(boo1)

# 获取当前页面的句柄
handler1 = driver.current_window_handle
# 获取所有句柄
handlers = driver.window_handles
# 将driver绑定的句柄进行变更
driver.switch_to.window(handler1)

driver.quit()
