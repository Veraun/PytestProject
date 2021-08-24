#!/usr/bin/env python
# encoding: utf-8
'''
@author: sunsx
@software: pycharm
@file: main_page.py
@time: 2021/8/24 11:58 上午
@desc:
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

from Project_selenium.login_page.login_page import LoginPage
from Project_selenium.login_page.register_page import RegisterPage


class MainPage:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.implicitly_wait(3)


    def goto_register(self):
        """
        从首页-注册页
        :return:
        """
        self.driver.find_element(By.XPATH,'//*[@class="index_head_info_pCDownloadBtn"]').click()
        # 将类进行初始化
        return RegisterPage(self.driver)

    def goto_login(self):
        """
        从首页-登陆页-注册页
        :return:
        """
        self.driver.find_element(By.XPATH,'//*[@class="index_top_operation_loginBtn"]').click()
        return LoginPage(self.driver)

