#!/usr/bin/env python
# encoding: utf-8
'''
@author: sunsx
@software: pycharm
@file: test_fixture_auto.py
@time: 2021/5/21 11:48 上午
@desc:
'''
from datetime import datetime

import pytest

# scope 通过控制作用域来改变连接次数，例如数据库连接操作
@pytest.fixture(scope="module")
def login():
    print("登陆操作")
    token = datetime.now()
    yield token   #yield相当于return
    print("注销操作")
    # return token

@pytest.fixture()
def get_username(login):
    name = "赫敏"
    print(name)
    return name


def test_search(get_username):
    print("搜索")


def test_shop(login):
    print(login)
    print("购物")

def test_order():
    print("下单")
