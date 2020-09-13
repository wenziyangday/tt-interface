# -*- coding: utf-8 -*-


# 基本类型
class BaseTypeResponse:
    IS_NULL = '是个空值'
    IS_NUM = '是个数值'
    IS_STR = '是个字符串'
    IS_LIST = '是个列表'
    IS_TUPLE = '是个元组'
    IS_DICT = '是个字典'


# 基本类型报错
class BaseTypeError:
    IS_NOT_NULL = '不是个空值'
    IS_NOT_NUM = '不是个数值'
    IS_NOT_STR = '不是个字符串'
    IS_NOT_LIST = '不是个列表'
    IS_NOT_TUPLE = '不是个元组'
    IS_NOT_DICT = '不是个字典'
    IS_NOT_EQUAL = '不是相同类型'


# 接口响应code
class BaseCode:
    SUCCESS = 200
    ERROR = 400


# 接口响应对应message
class BaseCodeMsg:
    SUCCESS = '接口成功'
    ERROR = '接口报错'
