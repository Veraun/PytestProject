#!/usr/bin/env python
# encoding: utf-8
'''
@author: sunsx
@software: pycharm
@file: conftest.py
@time: 2021/5/21 2:57 下午
@desc:
'''
import pytest


@pytest.fixture(scope="session")
def login():
    print("登陆操作=========")
    name = "哈利波特"
    yield name   #yield相当于return
    print("注销操作")