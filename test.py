#encoding=utf-8

import time

import jieba_helper

import recommend_helper

import question_helper

import ocr_helper
import url_helper
content = url_helper.get_result_content("你好", 1)
print(content)
# question_body = question_helper.parse_question_and_answer((ocr_helper.baidu_ocr(r'C:/Users/pzima/PycharmProjects/auto_recommend/img/1576762015_compressed.png')))
# question = '千门万户曈曈日，总把新桃换旧符'
# for i in [0,1,2,3]:
#     q = jieba_helper.jieba_parse(question, i)
#     print(q)
#     question_body = [
#         True,
#         q,
#         ["王安石","白居易","苏轼"]
#         ]
#     recommend_helper.recommend_fast(question_body)
#     time.sleep(3)
#
# # import jieba.analyse
# # # from optparse import OptionParser
# #
# # content = "影视领域常用的“杀青”一词,最初是哪项"
# # tags = jieba.analyse.extract_tags(content, topK=10)
# #
# # print(" ".join(tags))