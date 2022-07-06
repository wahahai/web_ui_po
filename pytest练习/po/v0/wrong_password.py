""""密码错误测试用例"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()
driver.implicitly_wait(10)
# 点击首页登录按钮
driver.find_element(By.XPATH, '//*[@id="s-top-loginbtn"]').click()
# 输入一个不存在的用户名
driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_11__userName"]').send_keys("17611055692")
# 输入密码
driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_11__password"]').send_keys("666888")
# 点击登录按钮
driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_11__submit"]').click()
# 获取错误提示信息
sleep(2)
msg = driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_11__error"]').text
print("错误信息为:", msg)
driver.quit()










