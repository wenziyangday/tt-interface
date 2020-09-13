# -*- coding: utf-8 -*-
from utils.constant import BaseCode, BaseCodeMsg


# 响应值断言
class ResponseAssetsUtil:
    def __init__(self, code):
        self.code = code

    def solution(self):
        if self.code == BaseCode.SUCCESS:
            return BaseCodeMsg.SUCCESS
        if self.code == BaseCode.ERROR:
            return BaseCodeMsg.ERROR
