#encoding=utf-8
from PIL import Image
import colorsys
import os,base64,json
import pytesseract
import time
import re
import urllib,urllib2
import jieba_helper
import ocr_helper
import question_helper
import recommend_helper
import screen_shot_helper
import selenium_helper
import url_helper
import config
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
reload(sys) 
sys.setdefaultencoding('utf8')

question = '千门万户曈曈日，总把新桃换旧符'
print question
for i in [0,1,2,3]:
    q = jieba_helper.jieba_parse(question, i)
    print q
    question_body = [
        True,
        q,
        ["王安石","白居易","苏轼"]
        ]
    recommend_helper.recommend_fast(question_body)
    time.sleep(3)