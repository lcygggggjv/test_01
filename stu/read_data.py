
import openpyxl
from openpyxl.worksheet.worksheet import Worksheet
import yaml


def read_excel(file_path, sheet_name):
    """使用openpyxl库，读取excel数据，
    传入excel文件，sheet名称，类型注解，为WorkSheet
    只取表头，后取剩余单元格数据,列表推导式，for循环，取出单个row数据。
    使用zip函数，拼接对应成键值对形式
    dict转换成字典，最后嵌套列表里
    """
    work = openpyxl.load_workbook(file_path)

    sheet: Worksheet = work[sheet_name]

    datas = list(sheet.values)

    title = datas[0]

    rows = datas[1:]

    datas = [dict(zip(title, row)) for row in rows]

    return datas


def read_yaml(yaml_path):

    with open(yaml_path, encoding="utf-8") as f:

        datas = list(yaml.safe_load_all(f))

        return datas


if __name__ == '__main__':

    data = read_yaml(r"D:\abc_new\test_class\stu\demo.yaml")

    print(data)
