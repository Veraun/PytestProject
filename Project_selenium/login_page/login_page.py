#!/usr/bin/env python
# encoding: utf-8
'''
@author: sunsx
@software: pycharm
@file: login_page.py
@time: 2021/8/24 12:00 下午
@desc:
'''
from selenium.webdriver.common.by import By

from Project_selenium.login_page.register_page import RegisterPage


class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    def scan(self):
        pass

    def goto_register(self):
        self.driver.find_element(By.XPATH,'//*[@class="login_registerBar_link"]').click()
        return RegisterPage(self.driver)