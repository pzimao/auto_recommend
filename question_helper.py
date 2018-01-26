#encoding=utf-8
from PIL import Image
import colorsys
import os,base64,json
import pytesseract
import time
import re
import urllib,urllib2
import config
import jieba_helper
import ocr_helper
import question_helper
import recommend_helper
import screen_shot_helper
import selenium_helper
import url_helper
import threading
import win32gui, win32ui, win32con
# import win32api
from selenium import webdriver
# import traceback
from selenium.webdriver.support.wait import WebDriverWait
# import urllib, urllib2
# import StringIO 
from aip import AipOcr
import operator
import jieba
import random
import requests
import thread
from lxml import html
import sys
from decorator import append
reload(sys) 
sys.setdefaultencoding('utf8')


def parse_false(question):
    for item in config.FALSE:
        if item in question:
            question = question.replace(item, " ")
            return question, False
    return question, True


def parse_question_and_answer(question):
    q = re.findall(re.compile(r'^(\d+\.?)'),question)
    real_question = question
    if len(q) > 0: 
        real_question = question[len(q[0]):]
    
    ans_ls = []
#     print real_question
    line_ls = real_question.split('||')
    if len(line_ls)>3:
        ans_a = line_ls[-4].strip()
        ans_b = line_ls[-3].strip()
        ans_c = line_ls[-2].strip()
        ans_ls.append(ans_a)
        ans_ls.append(ans_b)
        ans_ls.append(ans_c)
    else:
        print '选项没能解析出来'
        ans_ls = ["_","_","_"]
    real_question = "".join(line_ls[0:-4])
#     real_question = real_question.replace('\"',"")
    real_question, true_flag = parse_false(real_question)
#     pattern_a = r'A.\s?([\w\W\d]+)B.'
#     pattern_b = r'B.\s?([\w\W\d]+)[Cc].'
#     pattern_c = r'[cC].\s?([\w\W\d]+)'
#     ans_a = re.compile(pattern_a)
#     ans_b = re.compile(pattern_b)
#     ans_c = re.compile(pattern_c)
#     ans_ls = []
#     a = re.findall(ans_a, question)
#     b = re.findall(ans_b, question)
#     c = re.findall(ans_c, question)
#     if len(a) >0:
#         ans_ls.append(a[0])
#     if len(b) >0:
#         ans_ls.append(b[0])
#     if len(c) >0:
#         ans_ls.append(c[0])
#     return true_flag, real_question, ans_ls
    
#     real_question = ''.join(question.split('|').remove(ans_a).remove(ans_b).remove(ans_c))
    print '原问题:',
    print real_question
    real_question = jieba_helper.jieba_parse(real_question)
    for i in config.word_escape:
        if i in real_question:
            real_question = real_question + " "+config.word_escape[i]
    return true_flag, real_question, ans_ls
def process_question(question):
    #对问题进行处理
    if question.count("\"")%2 == 1:
#         #需要去掉一个"
        question = question.replace("\"","")     
#     question = "".join([e.strip("\r\n") for e in question if e])
    return question