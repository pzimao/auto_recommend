# encoding=utf-8
import re
import config
import jieba_helper


def parse_false(question):
    for item in config.FALSE:
        if item in question:
            question = question.replace(item, " ")
            return question, False
    return question, True


def parse_question_and_answer(question):
    q = re.findall(re.compile(r'^(\d+\.?)'), question)
    real_question = question
    if len(q) > 0:
        real_question = question[len(q[0]):]

    ans_ls = []
    #     print real_question
    line_ls = real_question.split('||')
    if len(line_ls) > 3:
        ans_a = line_ls[-4].strip()
        ans_b = line_ls[-3].strip()
        ans_c = line_ls[-2].strip()
        ans_0 = line_ls[-5].strip()  # 有的题目是4个选项
        ans_ls.append(ans_a)
        ans_ls.append(ans_b)
        ans_ls.append(ans_c)
        if "?" not in ans_0:
            ans_ls.append(ans_0)
    else:
        print('选项没能解析出来')
        ans_ls = ["", "", ""]
    real_question = "".join(line_ls[0:-4])
    real_question, flag = parse_false(real_question)
    print('原问题:'),
    print(real_question)
    real_question = jieba_helper.jieba_parse(real_question)
    for i in config.word_escape:
        if i in real_question:
            real_question = real_question + " " + config.word_escape[i]
    return flag, real_question, ans_ls


def process_question(question):
    # 对问题进行处理
    if question.count("\"") % 2 == 1:
        #         #需要去掉一个"
        question = question.replace("\"", "")
    #     question = "".join([e.strip("\r\n") for e in question if e])
    return question
