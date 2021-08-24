#!/usr/bin/env python
# encoding: utf-8
'''
@author: sunsx
@software: pycharm
@file: test_yield.py
@time: 2021/5/21 2:46 下午
@desc:
'''
from datetime import datetime

import pytest

def test_search(login):
    print("搜索")


def test_shop(login):
    print(login)
    print("购物")
# @pytest.mark.usefixtures('login')
def test_order(login):
    print(login)
    print("下单")
