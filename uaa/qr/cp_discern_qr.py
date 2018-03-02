import base64
import os
from io import *

import requests

import uaa.qr.cp_img_read as img_read
from constains import AresTerraCons, ENV, getRootPath

# 图片存放路径
pic_path = "{}uaa{}qr{}img{}".format(getRootPath(), os.sep, os.sep, os.sep)


def save_img(hex_str, path, name, type=None):
    """将16进制的字符串保存为图片"""
    imgdata = base64.b64decode(hex_str)
    file = open(path + name + "." + type, 'wb')
    file.write(imgdata)
    file.close()


def downloads_pic():
    """调用接口获取验证码流，保存为图片"""
    url = AresTerraCons().getDownloadPic()
    res = requests.get(url, stream=True)
    res = res.json()
    print(res['data']['clientId'], res['data']['code'], '\t')
    code = res['data']['code'].encode(encoding='utf-8')
    img_name = res['data']['clientId']
    save_img(code, pic_path, name=img_name, type='jpg')
    return img_name


def read_img_hex():
    """读取16进制图片信息"""
    aaa = open(pic_path + "1.jpg", 'rb')
    print(aaa.read())
    aaa.close()


def example(express, result=None):
    if result == None:
        result = eval(express)
    print(express, ' ==> ', result)


def get_current_code():
    img_name = downloads_pic()
    return (img_name, img_read.load_img_qr(img_name + ".jpg"))


# read_img_hex()
# print('16进制字符串', end=': ')
# example(r"bytes().fromhex('010210')")
#
# print("16进制字符串", end=": ")
# example("int('0x10', 16)")

if __name__ == '__main__':
    print(get_current_code())
