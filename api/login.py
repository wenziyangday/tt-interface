# -*- coding: utf-8 -*-
import requests


# 登录类
class Login:
    def __init__(self):
        self.req = requests.session()
        self.req.headers[
            'Authorization'] = 'Bearer 3.51466.WtySy-merCTnYR2tNqJTiMegVAPV-AABBKB-QkuRD027AMaAZrhAPLChtSPof_5ciQASOpyxRsgH_E493LNDYGHqerxWrqlYCCyxvwJbq4Eq2s5Kk6jPlBNmwzngWLVi0-fWVirYGIoVA-4MUsv-4AbLcs2NBLghkJaiU8ObwjMDpCMihVvAr41iAE8muO5uc_8YmTM4BqQhVNN-SLnjpwSsmjHv6WpR04WqhtAsFlA-8RErLq1bjKggwqvimQv_XffarRmzTrjiPDNpFf2Ckg'

    # 登录
    def login(self, url, params):
        res = self.req.post(url, data=params)
        print(res)
        pass

    # 登出
    def logout(self, url):
        print(self.req.headers)
        pass


if __name__ == '__main__':
    Login().login('https://cnodejs.org/api/v1/topic_collect/collect', {'data': 'asd'})
    Login().logout('https://cnodejs.org/api/v1/topic_collect/collect')
