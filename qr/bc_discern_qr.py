import base64
import os
from io import *
import requests
from qr.bc_img_read import *

# 图片存放路径
pic_path = '{}{}img{}bc{}'.format(os.getcwd(), os.sep, os.sep, os.sep)
normal_pic_path = pic_path + os.sep + "normal" + os.sep



# 将16进制的字符串保存为图片
def save_img(hex_str, path, name, type=None):
    imgdata = base64.b64decode(hex_str)
    file = open(path + name + "." + type, 'wb')
    file.write(imgdata)
    file.close()


# 调用接口获取验证码流，保存为图片
def downloads_pic(i):
    url = 'http://api.blr5589.com/v1/member/code/get?width=142&height=50'
    # url = 'http://api.blr5589.com/v1/member/code/get'
    res = requests.get(url, stream=True)
    print(res.json()['result']['code'])
    code = res.json()['result']['code'].encode(encoding='utf-8')
    save_img(code, normal_pic_path, name='bc_verify_code_' + str(i), type='jpg')


# 读取16进制图片信息
def read_img_hex():
    aaa = open(normal_pic_path + "1.jpg", 'rb')
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
    # for i in range(30):
    #     downloads_pic(i)
    # for i in range(0, 30):
    #     load_img_qr_2(str(i))
    for i in range(0,30):
        load_img_qr(i)
