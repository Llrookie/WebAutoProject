import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('https://www.nowcoder.com/exam/company')
time.sleep(3)
# 使用select()可选择下拉框的内容
sel = Select(driver.find_element(By.XPATH,'/html/body/section/main/div/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div/input'))
# 三种定位方式
# sel.select_by_index('下标')
sel.select_by_value('产品/运营')   # 标签里的 value = 'value值'
# sel.select_by_visible_text('文本内容')
time.sleep(3)
