#!/usr/bin/env python
# encoding: utf-8
'''
@author: sunsx
@software: pycharm
@file: conftest.py
@time: 2021/5/21 2:44 下午
@desc:
'''

#文件名称是固定的，不能改

# scope 通过控制作用域来改变连接次数，例如数据库连接操作
from datetime import datetime
from typing import List

import pytest


@pytest.fixture(scope="session")
def login():
    print("登陆操作=========")
    token = datetime.now()
    yield token   #yield相当于return
    print("注销操作")


def pytest_collection_modifyitems(
        session:"Session",config:"Config",items:List["Items"]
) ->None:
    print(items)
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item._nodeid.encode('utf-8').decode('unicode-escape')
        if 'add' in item._nodeid:
            item.add_marker(pytest.mark.add)

    items.reverse()