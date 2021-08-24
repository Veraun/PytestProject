#!/usr/bin/env python
# encoding: utf-8
'''
@author: sunsx
@software: pycharm
@file: test_order.py
@time: 2021/5/24 10:29 下午
@desc:
'''

import pytest


@pytest.mark.second
def test_foo():
    assert True


@pytest.mark.first
def test_bar():
    assert True
