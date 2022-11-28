import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# 打开浏览器
driver = webdriver.Chrome()
# 打开百度页面
driver.get('https://baidu.com')
# 定位元素并赋值，id定位
driver.find_element(By.ID, 'kw').send_keys('python学习')
# name定位
# driver.find_element(By.NAME, 'wd').send_keys('今天你快乐了吗')
# 通过class name定位
# driver.find_element(By.CLASS_NAME, 's_ipt').send_keys('我很快乐')
# link_text定位
# driver.find_element(By.LINK_TEXT,'新闻').click()
# partial_link_text定位
# driver.find_element(By.PARTIAL_LINK_TEXT,'闻').click()

# xpath定位
# 绝对路径：/开头;
# 相对路径：//开头
"""
    1、相对路径+索引定位
        //form/span[1]/input
    2、相对路径+属性定位
        //*[@id="kw"]
    3、相对路径+通配符定位
        //*[@autocomplete="off"]
    4、相对路径+部分属性值定位
        以**开头：//*[start-with(@autocomplete,"of")],即元素autocomplete以of开头
        以**结尾：//*[substring(@autocomplete,2)="ff"],即元素autocomplete以ff结尾
        包含：//*[contains(@autocomplete,"of")],即元素autocomplete包含of
    5、相对路径+文本定位
        //span[text()='按图片搜索']
"""

# driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[5]/div/div/form/span[1]/input').send_keys('python学习')
# driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys('python学习')

# CSS定位
"""
    绝对路径：不用
    通过id和class定位
    通过属性定位
    通过部分属性定位
    查询子元素定位
    查询兄弟节点定位
"""
# driver.find_element(By.CSS_SELECTOR, '#kw').send_keys('有点溜')

# 点击搜索
driver.find_element(By.ID, 'su').click()
# 打开页面等待两秒
time.sleep(2)
# 退出浏览器
driver.quit()
