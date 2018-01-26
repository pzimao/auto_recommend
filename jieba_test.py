#encoding=utf-8
import sys
sys.path.append('../')

import jieba
import jieba.analyse
from optparse import OptionParser
import sys
reload(sys) 
sys.setdefaultencoding('utf8')

content = "影视领域常用的“杀青”一词,最初是哪项"
tags = jieba.analyse.extract_tags(content, topK=10)

print(" ".join(tags))