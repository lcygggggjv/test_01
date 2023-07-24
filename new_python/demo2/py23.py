from urllib3 import *

disable_warnings()

http = PoolManager()

# 指定要提交的 请求url ， /register是路由

# url = 'http://127.0.0.1:5000/register'
#
# rs = http.request('GET', url, fields={"name": "李宁", "age": 18})
#
# data = rs.data.decode('utf-8')
#
# print(data)

url = 'http://127.0.0.1:5000/upload'


while True:

    filename = input("请输入名称再当前目录下")

    if not filename:

        break

    with open(filename, 'rb') as f:

        filedata = f.read()

        rs = http.request('POST', url, fields={"file": (filename, filedata)})

        print(rs.data.decode('utf-8'))
