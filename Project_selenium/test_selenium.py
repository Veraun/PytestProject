#!/usr/bin/env python
# encoding: utf-8
'''
@author: sunsx
@software: pycharm
@file: test_selenium.py
@time: 2021/8/17 10:49 下午
@desc:
'''

from selenium import webdriver  # 导入webdriver

driver = webdriver.Chrome()  # 实例化Chrome浏览器
driver.get("https://www.baidu.com")  # 打开http://www.baidu.com
