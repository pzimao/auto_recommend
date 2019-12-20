# encoding=utf-8
import config
import urllib.request
import urllib.parse
import traceback


def get_result_content(keyword, ref=0):
    try:
        request = urllib.request.Request(config.ref_url[ref] + urllib.request.quote(keyword))

        request.add_header("user-agent",
                           "Mozilla/5.0 (Linux; U; Android 2.2; en-us; Sprint APA9292KT Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1")
        if ref == 1:
            request.add_header("HOST",
                               "zhidao.baidu.com")
            request.add_header("referer", "https://zhidao.baidu.com/search?ct=17&pn=0&tn=ikaslist&rn=10&fr=wwwt&word=bas")
        else:
            request.add_header("HOST",
                           "www.baidu.com")
        request.add_header("cookie",
                           "BAIDUID=A7017431EFDC367DFB45D3AB9718650E:FG=1; BIDUPSID=A7017431EFDC367DFB45D3AB9718650E; PSTM=1568443861; BD_UPN=12314753; MCITY=-75%3A; __cfduid=da2cfe108a9972f83967b36e65f2d95591575018510; yjs_js_security_passport=bea27660c95b9226fb43daa417ccb50a671a2a27_1576633697_js; BDUSS=ZWMXEtRW9uZVJ1Q0hUY1F3Sm1lRW5kdkRxcUFqSXg3bllabThwTzRlRkVSeUZlRUFBQUFBJCQAAAAAAAAAAAEAAADoKhiKyt61xE1lbW9yeQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAES6-V1EuvldRj; delPer=0; BD_CK_SAM=1; PSINO=1; ZD_ENTRY=baidu; BD_HOME=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; COOKIE_SESSION=13941_0_9_0_8_24_1_3_9_6_1_6_0_0_15_0_1575257028_0_1576661115%7C9%230_0_1576661115%7C1; H_PS_PSSID=1466_21101_30211_18560_30284_26350; sug=3; sugstore=0; ORIGIN=0; bdime=0; H_PS_645EC=3ec2pYPJ4RASm6xFH3rYwmiocwEx%2B8Ut37eOntpbY0oECx3dInvBvfR0TL4")
        response = urllib.request.urlopen(request)
        return str(response.read(), encoding="utf8")
    except:
        print('url 读取异常')
        traceback.print_exc()
