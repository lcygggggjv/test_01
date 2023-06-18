import base64

import requests
from ddddocr import DdddOcr

import utils


def recognition_down(img_url):
    """识别下载的图片验证码"""
    img = requests.get(img_url)

    ocr = DdddOcr()

    img_bytes = ocr.classification(img.content)

    return img_bytes

# s2 = recognition_open(r"D:\abc_new\test_class\imgs.png")
# print(s2)


# sd = recognition_down('http://spx.lemfix.com/?s=user/userverifyentry/type/user_login.html')
#
# print(sd)

def recognition_open(img_path):
    """识别本地保存的图片验证码,用with open打开图片用rb模式"""
    ""r"D:\abc_new\test_class\imgs.png"""

    with open(img_path, 'rb') as f:

        img = f.read()

    ocr = DdddOcr()

    img_byte = ocr.classification(img)

    return img_byte


def get_image_bytes(image_path):
    with open(image_path, 'rb') as f:
        image_bytes = f.read()
    return image_bytes


def shi(image_file):

    # with open(image_file, 'rb')as f:

    # ims = f.read()
    base_64 = base64.b64encode(image_file).decode("utf-8")

    return base_64


def admin_login(account, password, image_code):

    ress = requests.request(method="post",
                            headers={"content-type": "application/json"},
                            url="http://mall.lemonban.com:8108/adminLogin",
                            json={"principal": account, "credentials": password, "imageCode": image_code})
    try:
        con = ress.json()

    except:
        raise ValueError(f"通过文本显示，异常", ress.text)

    return con


if __name__ == '__main__':

    # img_code = recognition_down("http://mall.lemonban.com:8108/captcha.jpg?uuid=140fe575-e583-4445-84ae-2fc0631f153d")
    img_code = recognition_down("http://mall.lemonban.com:8108/captcha.jpg?uuid=140fe575-e583-4445-84ae-2fc0631f153d")
    # code = get_image_bytes(r"D:\abc_new\test_class\img.png")
    # img_code = shi(code)
    print(img_code)
    # print(code)
    # res = admin_login("student", "123456a", code)
    #
    # print(res)
