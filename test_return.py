#!/usr/bin/env python
# encoding: utf-8
'''
@author: sunsx
@software: pycharm
@file: test_return.py
@time: 2021/5/24 9:28 下午
@desc:
'''
import pytest


# @pytest.mark.flaky(reruns=5,reruns_delay=2)
def test_return():
    assert 1 == 1
    assert 1 == 2
    assert 2 == 3

    # pytest.assume(1 == 1)
    # pytest.assume(1 == 2)
    # pytest.assume(1 == 3)
