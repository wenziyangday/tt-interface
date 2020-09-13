# -*- coding: utf-8 -*-
from api.login import Login


# 请求处理
class RequestUtils:
    def __init__(self):
        # 此处使用login 是为了获取登录状态共享，其实就是每次登录自己手动调用登录
        # 从而生成一个新的登录状态
        self.req = Login().req

    # 不同请求类型发出不同的类型
    def method(self, method_type, url, params):
        if method_type == 'get':
            return self.req.get(url=url, params=params)
        elif method_type == 'post':
            return self.req.post(url=url, data=params)
        else:
            return '不确定类型'

    # 解析返回值并生成对应条件的二维数组数据，从而生成测试报告
    def load_response(self, method_type, url, params):
        response = self.method(method_type, url, params)
        # TODO 此处之后要做根据响应值得不同做出对应的处理，从而拼接出来生成的报告
        # TODO 返回值和hope（期待值）差异化比较，最终写入报告之中
        print(response.text)
        return response.text


if __name__ == '__main__':
    RequestUtils()
    Login()
