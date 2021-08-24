#!/usr/bin/env python
# encoding: utf-8
'''
@author: sunsx
@software: pycharm
@file: test_dependency.py
@time: 2021/5/24 10:38 下午
@desc:
'''
from time import sleep

import pytest


# @pytest.mark.dependency()
# @pytest.mark.xfail(reason="deliberate fail")
def test_a():
    sleep(3)
    assert False


# @pytest.mark.dependency()
def test_b():
    sleep(3)
    pass


# @pytest.mark.dependency(depends=["test_a"])
# c 依赖 a ,a不执行，则c 跳过
def test_c():
    sleep(3)
    pass


# @pytest.mark.dependency(depends=["test_b"])
def test_d():
    sleep(3)
    pass


# @pytest.mark.dependency(depends=["test_b", "test_c"])
# c 跳过，e也会跳过
def test_e():
    sleep(3)
    pass