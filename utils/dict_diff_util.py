# -*- coding: utf-8 -*-
from utils.constant import BaseTypeError


# 比较两个 dict 类型一致即为相同 （找出不是相同类型的值）
# cur当前值，target目标值
class DictDiffUtil:
    def __init__(self, cur_dict=None, target_dict=None):
        self.cur = cur_dict
        self.target = target_dict

    # null 判断
    @staticmethod
    def is_null(val=None):
        return val is None

    # 字符串判断
    @staticmethod
    def is_str(val=None):
        return isinstance(val, str)

    # 数字判断
    @staticmethod
    def is_num(val=None):
        return isinstance(val, int) or isinstance(val, float)

    # dict（字典） 判断
    @staticmethod
    def is_dict(val=None):
        return isinstance(val, dict)

    # tuple（元组） 判断
    @staticmethod
    def is_tuple(val=None):
        return isinstance(val, tuple)

    # list（列表） 判断
    @staticmethod
    def is_list(val=None):
        return isinstance(val, list)

    # 字典中key（键）的列表
    @staticmethod
    def key_dict_list(val=None):
        return list(dict.keys(val))

    # 字典中val（值）的列表
    @staticmethod
    def val_dict_list(val=None):
        return list(dict.values(val))

    # 两个值是否类型相同
    @staticmethod
    def equal_type(cur=None, target=None):
        return isinstance(cur, type(target))

    # 解决方法
    def solution(self):
        diff = {}

        # 基础元素只要不是dict，就直接跳出
        if not self.is_dict(self.cur) or not self.is_dict(self.target):
            return BaseTypeError.IS_NOT_DICT

        keys_cur = self.key_dict_list(self.cur)
        keys_target = self.key_dict_list(self.cur)
        for index, val in enumerate(keys_cur):
            print('index %s 值：%s' % (index, val))
            if val not in keys_target:
                return
            cur_val = self.cur[val]
            target_val = self.target[val]
            # 是否是相同类型
            if not self.equal_type(cur_val, target_val):
                diff[val] = target_val


'''
tips:
1.几种基础类型、复合类型（由基础类型组成）及其类型判断或者说获取数据类型
2.list（列表的遍历方式）
'''

if __name__ == '__main__':
    DictDiffUtil({'a': 'g'}, {'b': 'gg'}).solution()
