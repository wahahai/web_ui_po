# 测试类形式
import pytest


class TestDemo(object):  # 正常定义类，但是测试类名必须以 Test 开头
    """测试示例类"""

    def test_method1(self):  # 正常定义方法，但是测试方法名必须以 test 开头
        print("测试方法1")

    def test_method2(self):  # 正常定义方法，但是测试方法名必须以 test 开头
        print("测试方法1-2")

if __name__ == '__main__':
    # 语法: pytest.main(["-s", "文件名"])
    pytest.main(["-s", "test_case1.py"])
