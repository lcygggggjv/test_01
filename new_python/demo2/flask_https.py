import os

from flask import Flask, request


app = Flask(__name__)


@app.route('/register')
def register():

    # 打印名称为name的请求字段的值
    print(request.form.get('name'))

    # 打印名称为AGE的请求字段的值
    print(request.form.get('age'))

    # 向客户端返回注册成功
    return "注册成功"


@app.route('/upload', methods=['POST'])
def upload():

    file = request.files['file']

    if file:

        file.save(os.path.join(r'D:\abc_new\test_class\new_python\demo2\images', file.filename))

        return "文件上传成功"


@app.route('/')
def show():

    return "首页"


if __name__ == '__main__':

    app.run(debug=True)
