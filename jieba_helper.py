# encoding=utf-8
import re
import config
import jieba
import jieba.analyse


def jieba_parse(question, md=config.jieba_md):
    result = ''
    pattern1 = re.compile(r'(《[\w\W]*》)')
    fixed_word_ls = re.findall(pattern1, question)
    if len(fixed_word_ls) > 0:
        for i in fixed_word_ls:
            question = " ".join(question.split(i))
            result = result + i + " "
    if md == 0:
        seg_list = jieba.cut_for_search(question)  # 搜索引擎模式    
    if md == 1:
        seg_list = jieba.cut(question, cut_all=True)
    if md == 2:
        seg_list = jieba.cut(question, cut_all=False)
    if md == 3:
        seg_list = jieba.analyse.extract_tags(question, topK=config.search_keyword_num)
    for i in seg_list:
        if i in config.jieba_filter_ls:
            continue
        result = result + i + ' '
    return result
