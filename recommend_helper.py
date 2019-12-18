# encoding=utf-8
import url_helper
import re
import operator
import random
import threading
from lxml import html
import traceback


def recommend_fast(question_body, ref=0, ans=1):
    try:
        s = baidu_count(question_body, ref, ans)
        summary_li = sorted(s.items(), key=operator.itemgetter(1), reverse=True)
        result = ''
        if ref == 0:
            if ans == 0:
                result = result + '★'
            result = result + '百度搜索\n'
        else:
            if ans == 0:
                result = result + '★'
            result = result + '问答平台\n'
        for k in summary_li:
            result = result + str(k[1]) + '\t' + k[0] + '\n'
        print(result)
    except:
        traceback.print_exc()
        print('页面内容统计异常')


def recommend_accurate(question_body):
    s = baidu_count2(question_body)
    summary_li = sorted(s.items(), key=operator.itemgetter(1), reverse=True)
    print('关联程度')
    for k in summary_li:
        print(k[1]),
        print('\t'),
        print(k[0])


def baidu_count(question_body, ref=0, ans=1):
    keyword = question_body[1]
    answers = question_body[2]
    if ans == 1 and len(keyword) > 38:  # 加选项搜索
        for i in answers:
            keyword = keyword + " " + i

    content = url_helper.get_result_content(keyword, ref)
    summary = {
        ans: content.count(ans) for ans in answers
    }
    ans1 = answers[0]
    ans2 = answers[1]
    ans3 = answers[2]

    if ans1 in ans2:
        summary[ans1] = summary[ans1] - summary[ans2]
    if ans1 in ans3:
        summary[ans1] = summary[ans1] - summary[ans3]
    if ans2 in ans1:
        summary[ans2] = summary[ans2] - summary[ans1]
    if ans2 in ans3:
        summary[ans2] = summary[ans2] - summary[ans3]
    if ans3 in ans1:
        summary[ans3] = summary[ans3] - summary[ans1]
    if ans3 in ans2:
        summary[ans3] = summary[ans3] - summary[ans2]
    #     summary = {
    #         ans: resp.text.count(ans)
    #         for ans in answers
    #     }
    if all([cnt == 0 for cnt in summary.values()]):
        return summary

    default = list(summary.values())[0]
    if all([value == default for value in summary.values()]):
        answer_firsts = {
            ans: content.index(ans)
            for ans in answers
        }
        sorted_li = sorted(answer_firsts.items(), key=operator.itemgetter(1), reverse=False)
        answer_li, index_li = zip(*sorted_li)
        return {
            a: b
            for a, b in zip(answer_li, reversed(index_li))
        }
    return summary


def get_result_num(index, params, score):
    headers = {
        # "Cache-Control": "no-cache",
        "Host": "www.baidu.com",
        "User-Agent": random.choice(url_helper.Agents),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
    }
    #     resp = requests.get("http://www.baidu.com/s", params=params, headers=headers, timeout=2)
    #     if not resp.ok:
    #         print("baidu search error")
    #         return score.append((index,0))
    tree = html.fromstring(url_helper.get_result_content(params['wd']), 0)
    nums = tree.xpath("//div[@class='nums']/text()")
    if len(nums) > 0:
        result_nums = int(re.findall(re.compile(r'\d+'), nums[0].replace(',', ''))[0])
        #     print params['wd'],
        #     print result_nums
        score.append((index, result_nums))
    else:
        print('错误')
        result_nums = 0
        score.append((index, result_nums))


def baidu_count2(question_body):
    keyword = question_body[1]
    answers = question_body[2]
    params_ls = []
    for i in answers:
        params = {"wd": keyword + ' ' + i}
        params_ls.append(params)
        params = {"wd": i}
        params_ls.append(params)
    params_ls.append({"wd": keyword})
    score = []
    index = 0
    thread_ls = []
    for params in params_ls:
        thread1 = threading.Thread(target=get_result_num, args=(index, params, score))
        index = index + 1
        thread_ls.append(thread1)
        thread1.start()
    for t in thread_ls:
        t.join()

    tmp_ls = sorted(score, key=lambda i: i[0])
    score = []
    for i in tmp_ls:
        score.append(i[1])

    # 计算分数
    # K = count(Q&A) / (count(Q) * count(A))
    k_a = 0
    k_b = 0
    k_c = 0
    if score[-1] != 0:
        if score[1] != 0:
            k_a = int(score[0] * 100000000000.0 / (score[-1] * score[1]))
        if score[3] != 0:
            k_b = int(score[2] * 100000000000.0 / (score[-1] * score[3]))
        if score[5] != 0:
            k_c = int(score[4] * 100000000000.0 / (score[-1] * score[5]))

    s = [(answers[0], k_a), (answers[1], k_b), (answers[2], k_c)]
    ss = sorted(s, key=lambda i: i[1])
    ss = ss[::-1]
    result = '参考-关联程度:\n'
    for i in ss:
        result = result + i[0] + '\t' + str(i[1]) + '\n'
    print(result)
