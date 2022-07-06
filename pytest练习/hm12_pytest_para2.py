# pytest 参数化 多个参数
import pytest


class TestDemo(object):
    """示例测试类"""
    # 语法: @pytest.mark.parametrize("参数1, 参数n", [("数据1-1", "数据1-2"), ("数据2-1", "数据2-2"),。。。])
    # 注意:
    #     1. 多个参数必须置于同一个字符串内
    #     2. 数据格式必须是: [(), ()] or [[], []]

    @pytest.mark.parametrize("name, pwd", [("admin", "123456"), ("test", "555888"), ("ppp", "111888")])
    def test_method(self, name, pwd):
        """测试方法"""
        print("账号:%s 密码:%s" % (name, pwd))


if __name__ == '__main__':
    pytest.main(["-s", "hm12_pytest_para2.py"])