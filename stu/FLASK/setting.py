
from flask import Flask


class DefaultConfig:

    """
    默认配置
    """
    SECERT_KEY = 'CCCEEWEEW'


app = Flask(__name__, static_url_path='/s', static_folder='static')

# 设置
app.config.from_object(DefaultConfig)

# 定义视图
app.route('/')
def index():

    # 读取配置信息
    print(app.config['SECERT_KEY'])
    return 'hello word'


if __name__ == '__main__':

    app.run()
