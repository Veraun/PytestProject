#!/usr/bin/env python
# encoding: utf-8
'''
@author: sunsx
@software: pycharm
@file: test_address.py
@time: 2021/8/24 4:20 下午
@desc:
'''
from Project_selenium.address_page.main_page import MainPage


class TestAddress:

    def test_add_member(self):
        """
        从通讯录-添加成员
        :return:
        """
        main = MainPage()
        main.goto_address().add_member()