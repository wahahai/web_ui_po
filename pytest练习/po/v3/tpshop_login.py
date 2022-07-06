"""整合多个脚本至同一个测试用例中"""
import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest练习.po.utils import DriverUtil, get_alert_msg


class TestLogin(object):
    """登录测试类"""

    def setup_class(self):
        # self.driver = webdriver.Chrome()
        # self.driver.get("http://www.baidu.com")
        # self.driver.maximize_window()
        # self.driver.implicitly_wait(10)
        self.driver = DriverUtil.get_driver()   # 获取浏览器对象

    def teardown_class(self):
        # sleep(2)
        # self.driver.quit()
        DriverUtil.quit_driver()   # 退出浏览器对象

    def setup(self):
        # 打开首页
        self.driver.get("http://www.baidu.com")
        # 点击登录
        self.driver.find_element(By.XPATH, '//*[@id="s-top-loginbtn"]').click()

    def teardown(self):
        pass

    def test_account_does_not_exist(self):
        """账号不存在测试方法"""

        # 点击首页登录按钮
        self.driver.find_element(By.XPATH, '//*[@id="s-top-loginbtn"]').click()
        # 输入一个不存在的用户名
        self.driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_11__userName"]').send_keys("17611055691")
        # 输入密码
        self.driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_11__password"]').send_keys("666888")
        # 点击登录按钮
        self.driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_11__submit"]').click()
        # 获取错误信息
        # msg = self.driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_11__error"]').text
        # print("错误信息为:", msg)
        msg = get_alert_msg()
        print("错误信息为:", msg)

    def test_wrong_password(self):
        """密码错误测试方法"""

        # 点击首页登录按钮
        self.driver.find_element(By.XPATH, '//*[@id="s-top-loginbtn"]').click()
        # 输入一个不存在的用户名
        self.driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_11__userName"]').send_keys("17611055692")
        # 输入密码
        self.driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_11__password"]').send_keys("666888")
        # 点击登录按钮
        self.driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_11__submit"]').click()
        # 获取错误信息
        # msg = self.driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_11__error"]').text
        # print("错误信息为:", msg)
        msg = get_alert_msg()
        print("错误信息为:", msg)


if __name__ == '__main__':
    pytest.main(["-s", "tpshop_login.py"])

