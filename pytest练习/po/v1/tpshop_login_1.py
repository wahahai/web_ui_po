"""整合多个脚本至同一个测试用例中"""
import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By



class TestLogin(object):
    """登录测试类"""

    def test_account_does_not_exist(self):
        """账号不存在测试方法"""
        driver = webdriver.Chrome()
        driver.get("http://www.baidu.com")
        driver.maximize_window()
        driver.implicitly_wait(10)
        # 点击首页登录按钮
        driver.find_element(By.XPATH, '//*[@id="s-top-loginbtn"]').click()
        # 输入一个不存在的用户名
        driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_11__userName"]').send_keys("17611055691")
        # 输入密码
        driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_11__password"]').send_keys("666888")
        # 点击登录按钮
        driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_11__submit"]').click()
        # 获取错误提示信息
        sleep(2)
        msg = driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_11__error"]').text
        print("错误信息为:", msg)
        driver.quit()

    def test_wrong_password(self):
        """密码错误测试方法"""
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


if __name__ == '__main__':
    pytest.main(["-s", "tpshop_login_1.py"])











