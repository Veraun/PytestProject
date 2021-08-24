#!/usr/bin/env python
# encoding: utf-8
'''
@author: sunsx
@software: pycharm
@file: address_page.py
@time: 2021/8/24 4:10 下午
@desc:
'''
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class AddressPage:
    def __init__(self,driver):
        self.driver = driver

    def add_member(self):
        print("add_membber")

        def wait_time(driver):
            # 点击添加成员按钮
            """
            显示等待：
            若在添加成员页，出现"保存并继续添加"按钮，则代表已经进入下一页
            :param driver:
            :return:
            """
            self.driver.find_elements(By.XPATH,"//*[@class='qui_btn ww_btn js_add_member']")[-1].click()
            # eles = driver.find_elements(By.XPATH,"//*[@id='username']")
            eles = driver.find_elements(By.XPATH, "//*[@class='qui_btn ww_btn ww_btn_Blue js_btn_continue']")
            return len(eles) > 0
        WebDriverWait(self.driver,10).until(wait_time)

        sleep(1)
        # 添加姓名
        self.driver.find_element(By.XPATH,"//*[@id='username']").send_keys("今天是星期一03")
        # 添加账号
        self.driver.find_element(By.XPATH,'//*[@id="memberAdd_acctid"]').send_keys("happy@1")
        # 添加手机号
        self.driver.find_element(By.XPATH,'//*[@class="qui_inputText ww_inputText ww_telInput_mainNumber"]').send_keys("13011112221")
        # 点击保存
        self.driver.find_element(By.XPATH,'//*[@class="qui_btn ww_btn js_btn_save"]').click()
