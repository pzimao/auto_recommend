# encoding=utf-8
import time
import question_helper

question = '4.电影《中国合伙人》中,由主角创办的英语学||校叫什么名字?||新希望||新东方||新梦想||'
s = time.time()
print(question_helper.parse_question_and_answer(question))
e = time.time()
print(e - s)
