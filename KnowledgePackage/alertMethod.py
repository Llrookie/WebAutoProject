'''
    模式窗口：不关闭这个窗口，其他的操作一律无法操作
    非模式窗口：不用关闭窗口，也可以进行其他操作

    警告框-alert: 是一个模式窗口
        1、driver对象是在当前页面，但是不在alert上，无法去定位这个弹窗的元素
        2、driver.switch_to.alert():暂时将浏览器对象driver交给alert用
        3、可以对alert窗口做的事情：
            text:返回弹窗中的文字信息
            accept():接受现有警告，就是点击它的确认按钮
            dismiss():放弃现有警告，就是点击它的取消按钮
            send_keys():发送文本至警告框
'''

from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.maximize_window()
time.sleep(3)
# 控制鼠标悬浮到“设置”按钮上
setbutton = driver.find_element(By.ID, 's-usersetting-top')
# 将对“设置”按钮的操作行为封装到ActionChains，到这一步，鼠标对象已经知道要干啥了，还没开始
ActionChains(driver).move_to_element(setbutton).perform()
time.sleep(3)
driver.find_element(By.PARTIAL_LINK_TEXT, '搜索设置').click()
time.sleep(1)
# 修改搜索配置
driver.find_element(By.XPATH, '//*[@id="nr_2"]').click()
time.sleep(1)
# 点击保存设置
driver.find_element(By.XPATH, '//*[@id="se-setting-7"]/a[2]').click()

driver.find_element(By.LINK_TEXT)
time.sleep(1)
# 将浏览器对象交给alert用
dd = driver.switch_to.alert
time.sleep(1)
# 获取警告框的文本信息以及点击确定
str = dd.text
print(str)
# 点击确认和取消
# dd.accept()
dd.dismiss()
time.sleep(1)
# 关闭浏览器
driver.quit()
