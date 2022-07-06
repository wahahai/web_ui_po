import pytest

class TestDemo(object):
    """测试示例类"""
    # 说明: 特殊方法名写法固定,没有代码提示,需要手写
    # 注意: 函数级别执行顺序
    # 先 setup() -> 测试方法1 ->teardown()方法， 再setup()-> 测试方法2 -> teardown()方法
    def setup(self):
        """开始方法"""
        print("函数-->开始")

    def teardown(self):
        """结束方法"""
        print("函数-->结束")

    def test_method1(self):
        """示例测试方法"""
        print("测试方法1")

    def test_method2(self):
        """示例测试方法"""
        print("测试方法2")

if __name__ == '__main__':
    pytest.main(["-s", "hm05_pytest_basic_05.py"])

