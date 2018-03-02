import os

import pytesseract
from PIL import Image
from constains import getRootPath

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'

# 图片存放路径
pic_path = "{}uaa{}qr{}img{}".format(getRootPath(), os.sep, os.sep, os.sep)
normal_pic_path = pic_path


# 读取图片信息
def load_img_info_test_1():
    im = Image.open(pic_path + 'bc_verify_code0.jpg')
    print(im.format, im.size, im.mode, " ")


# 读取验证码的数字
def load_img_qr(img_name):
    im = Image.open(normal_pic_path + img_name)
    # im = im.convert('RGB')
    # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    # 拉长图像，方便识别。
    # im = im.resize((300, 80))
    vcode = pytesseract.image_to_string(im, config=tessdata_dir_config)
    vcode = vcode.replace(" ", "")
    print(img_name + " " + vcode)
    return vcode


if __name__ == '__main__':

    for i in range(0, 30):
        load_img_qr(i)
