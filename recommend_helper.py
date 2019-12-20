import url_helper
import operator
import traceback


def recommend_fast(question_body, ref=0, ans=1):
    try:
        s = baidu_count(question_body, ref, ans)
        summary_li = sorted(s.items(), key=operator.itemgetter(1), reverse=True)
        result = '带选项 : '
        if ref == 0:
            if ans != 0:
                result = '不' + result
            result = result + '百度搜索\n'

        for k in summary_li:
            result = result + str(k[1]) + '\t' + k[0] + '\n'
        print(result)
    except:
        traceback.print_exc()
        print('页面内容统计异常')



def baidu_count(question_body, ref=0, ans=1):
    keyword = question_body[1]
    answers = question_body[2]
    if ans == 1:  # 加选项搜索
        for i in answers:
            keyword = keyword + " " + i

    content = url_helper.get_result_content(keyword, ref)
    summary = {
        ans: content.count(ans) for ans in answers
    }
    ans1 = answers[0]
    ans2 = answers[1]
    ans3 = answers[2]
    ans0 = '?'
    if len(answers) > 3:
        ans0 = answers[3]
    # 去掉重复统计的，好蠢。。
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
    if ans0 != '?':
        if ans1 in ans0:
            summary[ans1] = summary[ans1] - summary[ans0]
        if ans2 in ans0:
            summary[ans2] = summary[ans2] - summary[ans0]
        if ans3 in ans0:
            summary[ans3] = summary[ans3] - summary[ans0]
        if ans0 in ans1:
            summary[ans0] = summary[ans0] - summary[ans1]
        if ans0 in ans2:
            summary[ans0] = summary[ans0] - summary[ans2]
        if ans0 in ans3:
            summary[ans0] = summary[ans0] - summary[ans3]

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
