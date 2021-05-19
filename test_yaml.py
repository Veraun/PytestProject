#!/usr/bin/env python
# encoding: utf-8
'''
@author: sunsx
@software: pycharm
@file: test_yaml.py
@time: 2021/5/19 2:12 下午
@desc:
'''
import yaml

def test_yaml():
    with open("./datas/calc.yaml") as f:
        datas = yaml.safe_load(f)
        print(datas)
        print( datas['add']['datas'] )