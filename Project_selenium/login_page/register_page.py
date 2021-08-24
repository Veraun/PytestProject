#!/usr/bin/env python
# encoding: utf-8
'''
@author: sunsx
@software: pycharm
@file: register_page.py
@time: 2021/8/24 11:59 上午
@desc:
'''
from selenium.webdriver.common.by import By


class RegisterPage:
    def __init__(self,driver):
        self.driver = driver

    def register(self):
        self.driver.find_element(By.XPATH,'//*[@id="corp_name"]').send_keys("xxxxxxx")

