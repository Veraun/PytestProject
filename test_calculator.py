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

sys.path.append( "./" )
print( sys.path )

def get_datas():
    with open("./datas/calc.yaml") as f:
        datas = yaml.safe_load(f)
    return (datas['add']['datas'],datas['add']['ids'])

# yaml json excel csv xml
#测试类
class TestCalc:
    # 前置条件
    datas:list = get_datas()
    def setup_class(self):
        self.calc = Calculator()
        print("-----开始测试计算器 setup_class-----")

    # 后置条件
    def teardown_class(self):
        print("-----开始测试计算器 setup_class-----")

    def setup(self):
         print("开始执行用例")

    def teardown(self):
        print("-----用例执行结束-----")

    # done：相加功能
    @pytest.mark.parametrize( "a,b,result", datas[0],ids=datas[1])
    def test_add(self, a, b, result):
        # calc = Calculator()
        print( f"a={a},b={b},result={result}" )
        assert result == self.calc.add(a, b)
        pass

    # done:相减功能
    @pytest.mark.parametrize("a,b,result",datas[0],ids=datas[1])
    def test_subtract(self,a,b,result):
        print(f"a={a},b={b},result={result}")
        assert result == self.calc.subtract(a,b)
        pass

    # done:相乘功能
    @pytest.mark.parametrize("a,b,result",datas[0],ids=datas[1])
    def test_Multiply(self,a,b,result):
        print(f"a={a},b={b},result={result}")
        assert result == self.calc.Multiply(a,b)
        pass

    # done:相除功能
    @pytest.mark.parametrize("a,b,result",datas[0],ids=datas[1])
    def test_div(self,a,b,result):
        print(f"a={a},b={b},result={result}")
        assert result == self.calc.div(a,b)
        pass



    # def test_add1(self):
    #     dates = [[1, 1, 2], [2, 1, 0], [1, 0, 1]]
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