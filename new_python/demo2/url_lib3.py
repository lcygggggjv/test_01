from urllib.parse import urlencode

from urllib3 import *

# urlencode 函数再urllib.parse模块中

# 调用disable_warnings函数可以阻止显示警告信息

print(urlencode({'wd': "百度"}))

# http = PoolManager()
# http.request('GET', url='https://www.baidu.com', fields={"wd": '百度一下我'})
disable_warnings()

http = PoolManager()

# 使用拼接字符串，然后使用urlencode方法，直接传入关键字参数
url = 'https://www.baidu.com/s?' + urlencode({"wd": "极客起源"})
print(url)

# 使用get方法，传入url
response = http.request('GET', url)

# 返回值使用utf-8进行解码
data = response.data.decode('utf-8')

print(data)

