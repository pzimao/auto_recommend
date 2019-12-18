# encoding=utf-8

from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFilter
import cv2
import time
import config

time1 = time.time()

########################自定义图像压缩函数############################
# filename1: 原图路径
# filename2: 压缩图路径
#
def compress(filename1, filename2):
    image = cv2.imread(filename1)
    res = cv2.resize(image, config.screen_shot_size, interpolation=cv2.INTER_AREA)
    cv2.imwrite(filename2, res)
    imgE = Image.open(filename2)
    imgEH = ImageEnhance.Contrast(imgE)
    img1 = imgEH.enhance(1)
    gray1 = img1.convert("L")
    gary2 = gray1.filter(ImageFilter.DETAIL)
    #     gary3 = gary2.point(lambda i: i * 0.9)
    #     gary3.save(filename2)
    gary2.save(filename2)
#     gray1.save(filename2)

if __name__ == '__main__':
    path = "E:/neon_workspace/auto_recommend/"
    filename1 = "1515924735.05.png"
    filename2 = "compress.jpg"
    compress(r'D:\gitRepository\img\huangrong\ce8a12904f6874a7c06b3c339fe4251d_2_3_art.jpeg', r'D:\gitRepository\img\huangrong\test.jpg')
    time2 = time.time()
    print('总共耗时：' + str(time2 - time1) + 's')
