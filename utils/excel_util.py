# -*- coding: utf-8 -*-
import datetime
import openpyxl
import os


# 转化
def two_arr_to_dict(arr):
    dict_arr = []
    for row in arr[1:]:
        row_dict = {}
        for cell_index in range(len(row)):
            row_dict[arr[0][cell_index]] = row[cell_index]
        dict_arr.append(row_dict)
    return dict_arr


# excel 操作
# 创建：指定目录创建一个指定名称的excel
# 读取：

def format_time():
    now = datetime.datetime.now()
    return now.strftime('%Y-%m-%d-%H-%M-%S')


class ExcelUtil:
    def __init__(self):
        self.wb = openpyxl.Workbook()
        self.ws = self.wb.active

    ''''
    功能描述：指定路径下写入指定数据的指定名称的excel
    name: 表的名称
    data: 表格中的数据(二维数组) data[i] 表示第i行 data[i][j] 表示第i行第j列
    '''

    def create_excel(self, name, list_data):
        # 获取上级目录 下的report 目录 并切换
        p_dir = os.path.abspath(os.path.join(os.getcwd(), '../report')).replace('\\', '/')
        os.chdir(p_dir)
        # 时间戳 防止文件重名
        str_now = format_time()
        for item in list_data:
            self.ws.append(item)
        self.wb.save(name + '-' + str_now + '.xlsx')
        print('文件生成功')

    def read_excel(self, name):
        # 用例存放目录
        p_dir = os.path.abspath(os.path.join(os.getcwd(), '../case')).replace('\\', '/')
        os.chdir(p_dir)
        self.wb = openpyxl.load_workbook(name, read_only=True)
        two_list = []
        # 多个sheet  这段多重循环就是为了把sheet 中的 单元转化出二维数组
        for sheet in self.wb:
            # 单个sheet中 row
            for item_row in sheet.rows:
                row_arr = []
                # 每行的单元格
                for cell in item_row:
                    row_arr.append(cell.value)
                two_list.append(row_arr)
        return two_arr_to_dict(two_list)


if __name__ == '__main__':
    # data = [
    #     ['中国', '北京'],
    #     ['韩国', '首尔'],
    #     ['日本', '东京'],
    #     ['泰国', '曼谷'],
    #     ['马来西亚', '吉隆坡'],
    #     ['越南', '河内'],
    #     ['朝鲜', '平壤'],
    #     ['印度', '新德里']
    # ]
    # ExcelUtil().create_excel('reports', data)

    excel = ExcelUtil().read_excel('api.xlsx')
