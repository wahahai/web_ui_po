"""整合多个脚本至同一个测试用例中"""
import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest练习.po.utils import DriverUtil, get_alert_msg
from pytest练习.po.v4.index_page import IndexTask
from pytest练习.po.v4.login_page import LoginTask


class TestLogin(object):
    """登录测试类"""

    def setup_class(self):
        self.driver = DriverUtil.get_driver()  # 获取浏览器对象
        self.index_task = IndexTask()   # 实例化首页业务层对象
        self.login_task = LoginTask()   # 实例化登录页面业务层对象

    def teardown_class(self):
        DriverUtil.quit_driver()  # 退出浏览器对象

    def setup(self):
        # 打开首页
        self.driver.get("http://www.baidu.com")

        self.index_task.go_to_login()   # 跳转登录

    def teardown(self):
        pass

    def test_account_does_not_exist(self):
        """账号不存在测试方法"""

        self.login_task.login_method('17611055691', '666888')
        # 获取错误信息
        msg = get_alert_msg()
        print("错误信息为:", msg)

    def test_wrong_password(self):
        """密码错误测试方法"""

        self.login_task.login_method('17611055692', '111888')
        # 获取错误信息
        msg = get_alert_msg()
        print("错误信息为:", msg)


if __name__ == '__main__':
    pytest.main(["-s", "tpshop_login.py"])
