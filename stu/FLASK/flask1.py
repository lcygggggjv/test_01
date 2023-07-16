
from flask import Flask

# 创建一个app对象  flask('模块名字符串类型') 当前启动文件的目录当成工程目录
# app = Flask(__name__)

# /sd当做静态文件，不需要写全文件名  static_folder指明对应目录
app = Flask(__name__, static_url_path='/s', static_folder='static')

# 定义视图和路由
@app.route('/')
def index():

    return "hello word"


if __name__ == '__main__':
    # 整个入口函数, 命令行输入 python+ 文件名  调试服务器
    app.run()

