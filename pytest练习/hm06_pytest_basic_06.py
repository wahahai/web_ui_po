import pytest

class TestDemo(object):
    """测试示例类"""
    # 说明: 特殊方法名写法固定,没有代码提示,需要手写
    # 注意: 类级别执行顺序
    # 先 setup_class() -> 测试方法1 -> 测试方法2 -> teardown_class()方法
    def setup_class(self):
        """开始方法"""
        print("类-->开始")

    def teardown_class(self):
        """结束方法"""
        print("类-->结束")

    def test_method1(self):
        """示例测试方法"""
        print("测试方法1")

    def test_method2(self):
        """示例测试方法"""
        print("测试方法2")

if __name__ == '__main__':
    pytest.main(["-s", "hm06_pytest_basic_06.py"])

