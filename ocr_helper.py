# encoding=utf-8
from PIL import Image
import config
from aip import AipOcr

def baidu_ocr(img, api_version=5, timeout=6):
    app_id = config.baidu_ocr['app_id']
    app_key = config.baidu_ocr['app_key']
    app_secret = config.baidu_ocr['app_secret']
    client = AipOcr(appId=app_id, apiKey=app_key, secretKey=app_secret)
    client.setConnectionTimeoutInMillis(timeout * 1000)
    options = {}
    options["language_type"] = "CHN_ENG"
    with open(img, "rb") as fp:
        fp = fp.read()
        result = ''
        if api_version == 1:
            result = client.basicAccurate(fp, options)
        else:
            result = client.basicGeneral(fp, options)
        if "error_code" in result:
            print("baidu api error: ", result["error_msg"])
            return ""
        txt = ''
        try:
            for line in result['words_result']:
                txt = txt + line['words'] + '||'
            return txt
        except:
            return ''

def get_question(img_name):
    # 调用各种ocr，提取图片中的文字
    for i in config.ocr_prefer:
        question = ''
        if 'baidu' == i:
            question = baidu_ocr(img_name)

        if question != '':
            print("文字识别采用: " + i)
            return question
    return ''
