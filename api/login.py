# -*- coding: utf-8 -*-
import requests


# 登录类
class Login:
    def __init__(self):
        self.req = requests.session()
        pass

    # 登录
    def login(self, url, params):
        self.req.headers['token'] = 'TOKEN'
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
