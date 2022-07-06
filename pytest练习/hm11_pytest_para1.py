# pytest 参数化 单个参数
import pytest


class TestDemo(object):
    """示例测试类"""

    # 语法: @pytest.mark.parametrize("参数变量", ["数值1", "数值2", "数值3"。 。。。。])
    @pytest.mark.parametrize("name", ["小明", "小刚", "小红", "张三"])
    def test_method(self, name):
        """测试方法"""
        print("获取的名字是:", name)

if __name__ == '__main__':
    pytest.main(["-s", "hm11_pytest_para1.py"])
