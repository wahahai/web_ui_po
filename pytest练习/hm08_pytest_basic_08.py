# 控制函数执行顺序
import pytest

class TestDemo(object):
    """示例测试类"""
    # 语法: @pytest.mark.run(order=序号)
    # 注意: run(order=序号) 没有代码提示,需要手写

    @pytest.mark.run(order=3)
    def test_method1(self):
        """测试方法1"""
        print("测试方法1")

    @pytest.mark.run(order=2)
    def test_method2(self):
        """测试方法2"""
        print("测试方法2")

    @pytest.mark.run(order=1)
    def test_method3(self):
        """测试方法3"""
        print("测试方法3")


