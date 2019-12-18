# encoding=utf-8
from PIL import Image
import colorsys
import os
import win32gui, win32ui, win32con


# 截图
# savepath: 截图保存路径
# 截图起始点
# 截图大小
def screen_capture(savepath, position=(0, 0), size=(1920, 1080)):
    try:
        hwnd = 0
        hwndDC = win32gui.GetWindowDC(hwnd)
        mfcDC = win32ui.CreateDCFromHandle(hwndDC)
        saveDC = mfcDC.CreateCompatibleDC()
        saveBitMap = win32ui.CreateBitmap()
        saveBitMap.CreateCompatibleBitmap(mfcDC, size[0], size[1])
        saveDC.SelectObject(saveBitMap)
        saveDC.BitBlt((0, 0), size, mfcDC, position, win32con.SRCCOPY)
        saveBitMap.SaveBitmapFile(saveDC, savepath)
    except:
        print('截图异常')


def get_dominant_color(image):
    # 颜色模式转换，以便输出rgb颜色值
    image = image.convert('RGBA')
    # 生成缩略图，减少计算量，减小cpu压力
    image.thumbnail((200, 200))
    max_score = 0  # 原来的代码此处为None
    dominant_color = 0  # 原来的代码此处为None，但运行出错，改为0以后 运行成功，原因在于在下面的 score > max_score的比较中，max_score的初始格式不定
    for count, (r, g, b, a) in image.getcolors(image.size[0] * image.size[1]):
        # 跳过纯黑色
        #         if a == 0:
        #             continue
        #         
        saturation = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)[1]

        y = min(abs(r * 2104 + g * 4130 + b * 802 + 4096 + 131072) >> 13, 235)

        y = (y - 16.0) / (235 - 16)

        # 忽略高亮色
        #         if y > 0.9:
        #             continue

        # Calculate the score, preferring highly saturated colors.
        # Add 0.1 to the saturation so we don't completely ignore grayscale
        # colors by multiplying the count by zero, but still give them a low
        # weight.
        score = (saturation + 0.1) * count

        if score > max_score:
            max_score = score
            dominant_color = (r, g, b)

    return dominant_color


def isQuestion(imgpath):
    domain_color = get_dominant_color(Image.open(imgpath))
    if domain_color[0] < 210 or domain_color[1] < 210 or domain_color[2] < 210:
        #         print '---主持人废话，不处理',
        #         print domain_color
        os.remove(imgpath)
        return False
    print('*****题目来了******')
    return True
