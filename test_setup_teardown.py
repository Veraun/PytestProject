#!/usr/bin/env python
# encoding: utf-8
'''
@author: sunsx
@software: pycharm
@file: test_setup_teardown.py
@time: 2021/5/18 11:14 下午
@desc:
'''


def test_a():
    print("aaaaaaa")
    pass


def setup_function():
    print("测试前")


def teardown_function():
    print("测试后")
