# 通过time模块导入sleep
from time import sleep
# 通过selenium模块导入by包
from selenium.webdriver.common.by import By
# 通过selenium模块导入webdriver包
from selenium import webdriver
# 导入ActionChains包（鼠标悬浮该功能）
from selenium.webdriver.common.action_chains import ActionChains

# 实例化浏览器对象
driver = webdriver.Chrome()
# 打开网页
driver.get("https://www.baidu.com")
# 展示效果
# sleep(2)
# 输入小米
driver.find_element(By.ID, 'kw').send_keys("小米")
# driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys("小米")
# 点击百度一下
driver.find_element(By.XPATH, '//*[@id="su"]').click()
sleep(3)
# 关闭页面
driver.quit()