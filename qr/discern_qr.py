import base64
import os
from io import *
import requests

# 图片存放路径
pic_path = '{}{}img{}cp{}normal{}'.format(os.getcwd(), os.sep, os.sep, os.sep, os.sep)


# 将16进制的字符串保存为图片
def save_img(hex_str, path, name, type=None):
    imgdata = base64.b64decode(hex_str)
    file = open(path + name + "." + type, 'wb')
    file.write(imgdata)
    file.close()


# 调用接口获取验证码流，保存为图片
def downloads_pic(i):
    # url = 'http://121.58.234.210:19093/uaa/apid/member/code/get?width=142&height=50'
    url = 'http://api.88bccp.com/uaa/apid/member/code/get?width=142&height=50'
    res = requests.get(url, stream=True)
    res = res.json()
    print(res['data']['clientId'], i, res['data']['code'], '\t')
    code = res['data']['code'].encode(encoding='utf-8')
    save_img(code, pic_path, name='verify_code_' + str(i), type='jpg')


# 读取16进制图片信息
def read_img_hex():
    aaa = open(pic_path + "1.jpg", 'rb')
    print(aaa.read())
    aaa.close()


def example(express, result=None):
    if result == None:
        result = eval(express)
    print(express, ' ==> ', result)


# read_img_hex()
print('16进制字符串', end=': ')
example(r"bytes().fromhex('010210')")

print("16进制字符串", end=": ")
example("int('0x10', 16)")

if __name__ == '__main__':
    for i in range(30):
        downloads_pic(i)
