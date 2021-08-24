#!/usr/bin/env python
# encoding: utf-8
'''
@author: sunsx
@software: pycharm
@file: main_page.py
@time: 2021/8/24 2:39 下午
@desc:
'''
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from Project_selenium.address_page.address_page import AddressPage


class MainPage:
    def __init__(self):
        # 声明Chrome的参数
        chrome_arg = webdriver.ChromeOptions()
        # 加入调试地址
        chrome_arg.debugger_address = '127.0.0.1:9222'

        self.driver = webdriver.Chrome(options=chrome_arg)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def goto_address(self):
        # 打开通讯录功能
        sleep(1)
        self.driver.find_element(By.XPATH,"//*[@id='menu_contacts']").click()
        return AddressPage(self.driver)
