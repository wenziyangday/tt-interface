# -*- coding: utf-8 -*-
import os

import yaml


# yaml文件读写
class YamlUtil:
    def __init__(self):
        pass

    # 写入yaml类型文件
    @staticmethod
    def read_yaml(file):
        p_dir = os.path.abspath(os.path.join(os.getcwd(), '../config')).replace('\\', '/')
        os.chdir(p_dir)
        f = open(file, 'r', encoding='utf-8')
        cont = f.read()
        content = yaml.load(cont, Loader=yaml.FullLoader)
        return content

    # 读取yaml类型文件
    # 这里需要说明的是 存入数据的数据结构 具体参考文档 README.md
    @staticmethod
    def write_yaml(file, data):
        p_dir = os.path.abspath(os.path.join(os.getcwd(), '../config')).replace('\\', '/')
        os.chdir(p_dir)
        # a 表示追加写入，w 表示覆盖写入
        file_stream = open(file, 'a', encoding='utf-8')
        yaml.dump(data=data, stream=file_stream)


if __name__ == '__main__':
    data_dict = {
        "cookie1": {'domain': '.yiyao.cc', 'expiry': 1521558688.480118, 'httpOnly': False, 'name': '_ui_', 'path': '/',
                    'secure': False, 'value': 'HSX9fJjjCIImOJoPUkv/QA=='}}
    YamlUtil().write_yaml('test.yaml', data_dict)
    datas = YamlUtil().read_yaml('test.yaml')
    print(datas)
