'''
    隐式等待
        在创建driver对象后，设置一个全局的等待时间，对driver整个生命周期都有效；在等待时间内找到元素，继续执行下一步，超出时间找不到元素，则抛出异常
        driver.implicitly_wait(4);单位秒
        注意：在使用隐式等待时，实际上浏览器会一直刷新页面去寻找要找的元素

    显式等待
        就是明确的要等到某个元素的出现或者是某个元素的可点击条件，等不到就一直等，超时的话，就抛出异常
        用到的方法：
            WebDriverWait(driver,timeout,poll_frequency,ignored_exceptions=None) driver对象，超时时间，刷新频率
            until(method,message) 直到满足一个条件，返回结果；等不到就抛出message信息
                method:expected_conditions.presence_of_element_located(locator)  判断某个元素是否定位成功
                locator:By.ID;By.Name

    强制等待
        time.sleep(1),休眠，单位是秒，直接让线程休眠，啥事都不干

    注意：隐式等待优先级大于现实等待，若两者都设置了等待时间，以隐式等待时间为主

'''
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

# 隐式等待
# driver.implicitly_wait(10)

# 显示等待
# 等待百度首页的百度一下按钮显示出来，出来就点击，否则print()
ele = WebDriverWait(driver, 5, 0.5, ignored_exceptions=None).until(EC.presence_of_element_located((By.ID, 'su')),"找不到该元素")
print(ele)

# 关闭浏览器
driver.quit()
