"""
web自动化基本代码
"""
# 1. 导入模块
from time import sleep

from selenium import webdriver
# 2. 实例化浏览器对象
driver = webdriver.Chrome()
# 3. 打开网页
driver.get("http://www.baidu.com")
# 4. 观察效果
sleep(3)
# 5. 关闭页面
driver.quit()





