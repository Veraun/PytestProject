#!/usr/bin/env python
# encoding: utf-8
'''
@author: sunsx
@software: pycharm
@file: test_fixture_param.py
@time: 2021/5/21 3:25 下午
@desc:
'''
import pytest


@pytest.fixture(params=["harry","hemin"],ids=["aa","bb"])
def login(request):
    print("login")
    return request.param


def test_search(login):
    print(login)
    print("搜索")

