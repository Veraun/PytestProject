#!/usr/bin/env python
# encoding: utf-8
'''
@author: sunsx
@software: pycharm
@file: test_fixture.py
@time: 2021/5/21 10:39 上午
@desc:
'''
import pytest


@pytest.fixture()
def login():
    print("登陆")

@pytest.fixture()
def get_username():
    name = "赫敏"
    print(name)
    return name

def test_search():
    print("搜索")

#使用装饰器时，打印调用的函数获取不到函数返回值，只能打印出来内存地址，如果想要数据的返回值，可以在def test_shop(login):中调用
@pytest.mark.usefixtures("login")
def test_shop():
    print(login)
    print("购物")



# def test_order(login,get_username):
#     print("下单")
#  装饰器内部的先被执行，外部的后被执行
@pytest.mark.usefixtures("get_username")
@pytest.mark.usefixtures("login")
def test_order():
    print("下单")



