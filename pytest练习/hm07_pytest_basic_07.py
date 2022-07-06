import pytest

class TestDemo(object):
    """示例测试类"""
    # 执行顺序 1 - 3- 5- 4- 3- 6- 4- 2
    def setup_class(self):  # 1
        print("类级别-->开始")

    def teardown_class(self):  # 2
        print("类级别-->结束")

    def setup(self):            # 3
        print("函数级别-->开始")

    def teardown(self):          # 4
        print("函数级别-->结束")

    def test_method1(self):      # 5
        print("测试方法1")

    def test_method2(self):      # 6
        print("测试方法2")

if __name__ == '__main__':
    pytest.main(["-s", "hm07_pytest_basic_07.py"])




