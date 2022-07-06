"""公共方法模块: 习惯命名 utils"""
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_alert_msg():
    """获取弹窗信息方法"""
    sleep(2)
    msg = DriverUtil.get_driver().find_element(By.XPATH, '//*[@id="TANGRAM__PSP_11__error"]').text
    return msg


class DriverUtil(object):
    """浏览器对象管理类"""
    __driver = None   # 浏览器对象变量初始化状态

    @classmethod
    def get_driver(cls):
        """获取浏览器对象方法"""
        if cls.__driver is None:
            cls.__driver = webdriver.Chrome()   # 浏览器类型
            cls.__driver.get("http://www.baidu.com")   # 项目地址
            cls.__driver.maximize_window()    # 窗口最大化
            cls.__driver.implicitly_wait(10)   # 隐式等待
        return cls.__driver

    @classmethod
    def quit_driver(cls):
        """退出浏览器对象方法"""
        # 说明: 必须保证浏览器对象存在,才能执行退出操作
        if cls.__driver:    # 等价于: if self.driver is not None:
            sleep(2)
            cls.__driver.quit()
            cls.__driver = None    # 保险手段: 移除对象后, 保留对象变量, 以备下一次使用


if __name__ == '__main__':
    DriverUtil.get_driver()   # 获取浏览器对象
    sleep(2)
    DriverUtil.quit_driver()   # 退出浏览器对象






