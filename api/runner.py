# -*- coding: utf-8 -*-
from utils.excel_util import ExcelUtil
from utils.yaml_util import YamlUtil
from utils.request_util import RequestUtils
import json


class Runner:
    def __init__(self):
        pass

    @staticmethod
    def solution():
        excel_apis = ExcelUtil().read_excel('api.xlsx')
        params_common = YamlUtil().read_yaml('common.yaml')
        base_url = params_common['host']
        # 表头
        table_header = []
        # 具体接口对应的信息
        table_body = []
        # 将接口返回值，拼接到原来的dict上
        for item in excel_apis:
            url = base_url + item['url']
            params = json.loads(item['params'])
            response = RequestUtils().load_response(method_type=item['method'], url=url,
                                                    params={**params, **params_common['common']})
            item['back'] = response

        # print(excel_apis)

        # 将excel_apis 转化为二维数组写入excel
        for item in excel_apis:
            if len(table_header) == 0:
                table_header = list(dict.keys(item))
            #  数组添加元素
            item_value = list(dict.values(item))
            table_body.append(item_value)
        #  二维数组
        write_data = [table_header] + table_body
        ExcelUtil().create_excel(name='reports', list_data=write_data)


if __name__ == '__main__':
    Runner().solution()
