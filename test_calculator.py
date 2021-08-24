#!/usr/bin/env python
# encoding: utf-8
'''
@author: sunsx
@software: pycharm
@file: test_calculator.py
@time: 2021/5/15 12:30 下午
@desc:
'''
import pytest
import yaml

from PythonCode.Calculator import Calculator
import sys

sys.path.append("/")
print(sys.path)


def get_datas(name, type='int'):
    with open("datas/calc.yaml",encoding='utf-8') as f:
        datas = yaml.safe_load(f)
    all_datas = datas[name][type]['datas']
    ids = datas[name][type]['ids']
    return (all_datas, ids)


@pytest.fixture(scope="session")
def get_instance():
    print("-----开始测试计算器 setup_class-----")
    calc: Calculator = Calculator()
    yield calc
    print("-----结束测试计算器 setup_class-----")


# fixture param 传参
@pytest.fixture(params=get_datas('add', 'int')[0], ids=get_datas('add', 'int')[1])
def get_datas_with_fixture(request):
    print("test_param")
    return request.param


# 测试fixture pararm 传参
def test_param(get_datas_with_fixture):
    print( get_datas_with_fixture )


# yaml json excel csv xml
# 测试类
class TestCalc:
    # 前置条件
    # datas:list = get_datas()
    add_int_data = get_datas( 'add', 'int' )
    div_int_data = get_datas( 'div', 'int' )

    def setup_class(self):
        self.calc = Calculator()
        print("-----开始测试计算器 setup_class-----")

    # 后置条件
    def teardown_class(self):
        print("-----结束测试计算器 setup_class-----")

    def setup(self):
        print("开始执行用例")

    def teardown(self):
        print("-----用例执行结束-----")


    # done:相加功能
    def test_add(self, get_instance, get_datas_with_fixture):
        f = get_datas_with_fixture
        assert get_instance.add(f[0], f[1]) == f[2]
        # assert f[2] == f[0] + f[1]


    # done:相除功能
    # @pytest.mark.parametrize( "a,b,result", div_int_data[0], ids=div_int_data[1] )
    def test_div(self, get_instance, get_datas_with_fixture):
        # print( f"a={a},b={b},result={result}" )
        # if b == 0:
        #     with pytest.raises(ZeroDivisionError) as excinfo:
        #         self.calc.div(a,b)
        #     assert excinfo.type == ZeroDivisionError
        #     assert  "division by zero" in str(excinfo.value)
        # else:
        #     assert result == self.calc.div(a,b)
        try:
            f = get_datas_with_fixture
            assert get_instance.div(f[0],f[1]) == f[2]

        except ZeroDivisionError:
            return "除数不能为0"
        pass

    # done：相加功能
    # mark.parametrize 参数化 获取yaml文件传参
    # @pytest.mark.parametrize( "a,b,result", add_int_data[0], ids=add_int_data[1] )
    # def test_add(self, get_instance, a, b, result):
    #     # calc = Calculator()
    #     print( f"a={a},b={b},result={result}" )
    #     assert result == get_instance.add( a, b )
    #     pass

    # mark.parametrize 参数化 手动传参
    # @pytest.mark.parametrize("a,b,result",[
    #     [0.1,0.1,0.2],
    #     [0.2,0.1,0.3]
    # ])
    # def test_add_float(self,a,b,result):
    #     assert result == round(self.calc.add(a, b),2)

    # def test_add1(self):
    #     dates = [[1, 1, 2], [2, 1, 3], [1, 0, 1]]
    #     for data in dates:
    #         print(data)
    #         assert data[2] == self.calc.add(data[0], data[1])

    # class TestCalc:
# @pytest.mark.search
# def test_add(self):
#     calc = Calculator()
#     assert 2 == calc.add(1,1)
#     pass
#
# @pytest.mark.login
# def test_div(self):
#     pass
