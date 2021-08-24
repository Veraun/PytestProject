#!/usr/bin/env python
# encoding: utf-8
'''
@author: sunsx
@software: pycharm
@file: selenium_Wechat_Login.py
@time: 2021/8/21 2:30 下午
@desc:
'''
import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTmp():
    def setup(self):
        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address='127.0.0.1:9222'


        self.driver = webdriver.Chrome(options=chrome_arg)
        # self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_tmp(self):
        """
        基于首页登陆
        :return:
        """
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.find_element_by_css_selector(".index_top_operation_loginBtn").click()
        self.driver.find_element_by_css_selector(".login_registerBar_link").click()
        self.driver.find_element(By.ID,"corp_name").send_keys("xxx")
        # //*[@id="corp_name"]

        sleep(5)
        self.driver.close()

    def test_login_tmp(self):
        """
        基于浏览器复用后的内容进行操作
        :return:
        """
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.find_element_by_css_selector(".index_top_operation_loginBtn").click()
        sleep(5)
        self.driver.find_element(By.ID,"menu_contacts").click()


    def test_cookie_login(self):
        """
        利用cookie进行登录
        :return:
        """
        # cookies = self.driver.get_cookies()
        # with open('tmp.text','w',encoding="utf-8") as f:
        #       序列化
        #     json.dump(cookies,f)
        # print(cookies)

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1629537880'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'secure': False, 'value': ''}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850276016332'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '750722342'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325094447930'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850276016332'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a4824284'}, {'domain': '.qq.com', 'expiry': 1629624283, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1633652992.1629527563'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': '7vA23nyfko6NFWrNg8aGT_2OHVpMJwzE1CGVCJkqXFq5Bzr7Gm_VpfYBypiFZ2CI'}, {'domain': '.qq.com', 'httpOnly': False, 'name': 'pgv_info', 'path': '/', 'secure': False, 'value': 'ssid=s1661406464'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '22003895991198585'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'nKKQvS9vfR'}, {'domain': '.qq.com', 'expiry': 1632125277, 'httpOnly': False, 'name': 'lskey', 'path': '/', 'secure': False, 'value': '000100001413545cca7181830e06b680fddaa2c399fcf30d9b488088c7697e94ad695c5ced1b3a6f5b54b99c'}, {'domain': '.work.weixin.qq.com', 'expiry': 1632129886, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.qq.com', 'expiry': 1692609883, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.468030947.1616835149'}, {'domain': '.qq.com', 'expiry': 1930225450, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/', 'secure': False, 'value': 'de933a0d159e47a4'}, {'domain': '.work.weixin.qq.com', 'expiry': 1648371145, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'jZ_Tlfhb_m8GaK47Bkvb_9hfNEitf-nljgtX7jEokCSqlCLG-9nbLHkrcx3Knpuo8V_nTPhba5trZWpaitt0rv96YxZ_s-PeVMvGaOAUaG0CeXD1ZLcSVUftUx1dfFd9cHImpwgUvch3q7cb2y7VmUu3Uf03YT8YfqagJozbDahXSsuAeL_YETtWLStA78b6aPrkAGs_V0YnmcKO6_2Nx-QxeLzpesn9Hg3quI4B7SzQ5WDQkZWQK86Ctc_EZjKzlljXRSApTlYRkrLK6ynaZg'}, {'domain': '.work.weixin.qq.com', 'expiry': 1661073879, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1629527561,1629535522,1629537880'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'o_cookie', 'path': '/', 'secure': False, 'value': '985322725'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': '59203d68689c34e198743abc22e4f87ace29ec4077968fb9d8ef6e1558942a2f'}, {'domain': '.qq.com', 'expiry': 1629537941, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 1632125277, 'httpOnly': False, 'name': 'luin', 'path': '/', 'secure': False, 'value': 'o0985322725'}]

        with open("tmp.text","r",encoding="utf-8") as f:
            # 反序列化
            cookies = json.load(f)
        for i in cookies:
            self.driver.add_cookie(i)
        self.driver.refresh()
        sleep(6)

