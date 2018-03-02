import os
from array import array

import cv2
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'

custom_seq = '\\'

# 图片存放路径
pic_path = '{}{}img{}cp{}'.format(os.getcwd(), os.sep, os.sep, os.sep)
normal_pic_path = pic_path + os.sep + "normal" + os.sep
b_pic_path=pic_path + os.sep + "b" + os.sep
g_pic_path=pic_path + os.sep + "g" + os.sep

# 读取图片信息
def load_img_info_test_1():
    im = Image.open(pic_path + 'bc_verify_code0.jpg')
    print(im.format, im.size, im.mode, " ")


# 读取验证码的数字
def load_img_qr(i):
    img_name = 'g_verify_code_%s.jpg' % i
    im = Image.open(g_pic_path + img_name)
    # im = im.convert('RGB')
    # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    # 拉长图像，方便识别。
    # im = im.resize((300, 80))
    vcode = pytesseract.image_to_string(im, config=tessdata_dir_config)
    vcode= vcode.replace(" ","")
    print(img_name + " " + vcode)


def load_img_qr_1(i):
    img_name = 'bc_verify_code_%s.jpg' % i
    im = Image.open(normal_pic_path + img_name)
    im = im.convert('RGB')
    im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    # 拉长图像，方便识别。
    im = im.resize((200, 80))
    a = array(im)
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j][0] == 255:
                a[i][j] = [0, 0, 0]
            else:
                a[i][j] = [255, 255, 255]
    im = Image.fromarray(a)
    im.show()

    vcode = pytesseract.image_to_string(im, config=tessdata_dir_config)
    print(img_name + " " + vcode)


# 二值化
threshold = 140
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

rep = {'O': '0',
       'I': '1', 'L': '1',
       'Z': '2',
       'S': '8'
       }


def load_img_qr_2(i):
    name = 'verify_code_%s.jpg' % i
    # 打开图片
    im = Image.open(normal_pic_path + name)
    # 转化到灰度图
    imgry = im.convert('L')
    # 保存图像
    imgry.save(g_pic_path + 'g_' + name)
    # 二值化，采用阈值分割法，threshold为分割点
    out = imgry.point(table, '1')
    out.save(b_pic_path + 'b_' + name)
    # 识别
    text = pytesseract.image_to_string(out, config=tessdata_dir_config)
    print(text)
    # 识别对吗
    text = text.strip()
    text = text.upper()
    for r in rep:
        text = text.replace(r, rep[r])
        # out.save(text+'.jpg')
    print(text)
    return text


if __name__ == '__main__':
    for i in range(0, 30):
        load_img_qr_2(str(i))
    for i in range(0,30):
        load_img_qr(i)
