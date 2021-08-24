#!/usr/bin/env python
# encoding: utf-8
'''
@author: sunsx
@software: pycharm
@file: test_address.py
@time: 2021/8/22 11:36 上午
@desc:
'''
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestTmp():
    def setup(self):
        # 声明Chrome 的参数
        chrome_arg = webdriver.ChromeOptions()
        # 加入调试地址
        chrome_arg.debugger_address='127.0.0.1:9222'


        self.driver = webdriver.Chrome(options=chrome_arg)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_address(self):
        """
        复用已有的浏览器进行操作
        不可交互的元素：
        1、元素被遮挡，元素前边还有其他不可见元素
        2、元素有多个，需要人手工挑选中合适的元素
        :return:
        """
        # 打开通讯录功能
        self.driver.find_element(By.XPATH,"//*[@id='menu_contacts']").click()

        def wait_time(driver):
            self.driver.find_elements(By.XPATH,"//*[@class='qui_btn ww_btn js_add_member']")[1].click()
            eles = driver.find_elements(By.XPATH,"//*[@id='username']")
            return len(eles) > 0
        WebDriverWait(self.driver,10).until(wait_time)
        # 点击添加成员
        # self.driver.find_elements(By.XPATH,"//*[@class='qui_btn ww_btn js_add_member']")[1].click()
        # print(len(a))
        # self.driver.find_element(By.XPATH,'//*[@class="qui_btn ww_btn js_add_member"]').click()
        sleep(1)
        # 添加姓名
        self.driver.find_element(By.XPATH,"//*[@id='username']").send_keys("今天是星期一03")
        # 添加账号
        self.driver.find_element(By.XPATH,'//*[@id="memberAdd_acctid"]').send_keys("happy@1")
        # 添加手机号
        self.driver.find_element(By.XPATH,'//*[@class="qui_inputText ww_inputText ww_telInput_mainNumber"]').send_keys("13011112221")
        # 点击保存
        self.driver.find_element(By.XPATH,'//*[@class="qui_btn ww_btn js_btn_save"]').click()
