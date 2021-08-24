#!/usr/bin/env python
# encoding: utf-8
'''
@author: sunsx
@software: pycharm
@file: test_register.py
@time: 2021/8/24 12:30 下午
@desc:
'''
from time import sleep

from Project_selenium.login_page.main_page import MainPage


class TestRegister:
    def test_register(self):
         main = MainPage()
         main.goto_register().register()
         sleep(6)

    def test_login_register(self):
        main = MainPage()
        main.goto_login().goto_register().register()
        sleep(6)
