# auto_recommend
百万英雄答案自动搜索，辅助答题
程序功能
读取手机（模拟器）的题目，分词并在浏览器中进行百度搜索，控制台输出内容是选项与题目的关联程度，依据的是百度搜索，百度知道。

程序主要流程
1.屏幕截图-2.OCR识别题目-3.解析题目和选项-4.题目分词-5.selenium自动搜索-6.后台子线程打印各选项与题目的关联程度

1.在配置文件中设置截图区域（起始坐标和截图尺寸），为了保证OCR识别的准确性，截图尽量只包含题目部分。程序定时进行截图，依据截图的主体颜色来判断是不是题目。

2.如果出现题目，对题目截图进行压缩，调用百度云的OCR接口得到题目文字。

3.把题目和选线分开，认为每个选项占一行，所以题目文字的后三行就是选项。

4.调用jieba对题目进行分词，分词有几种模式，程序中使用的是测试过中发现的最准确的模式。

5.把选项作为关键词，连同题目关键词自动输入百度搜索框中，使用了selenium自动化测试工具，具体浏览器可以在程序中设置。

6.计算各选项和题目的关联程度，计算关联程度用的是别人提出的计算公式，我就不写了。我做了4种参考：
  6.1 在百度搜索，只输入题目关键词，统计各选项出现的次数
  6.2 在百度搜索，输入题目关键词和选项，统计各选项出现的次数
  6.3 在百度知道，只输入题目关键词，统计各选项出现的次数
  6.4 在百度搜索，利用关联度公式，计算出关联程度
  
在实际用的过程中，具体选哪种关联度做参考，需要看题目出题方式。比如：以下不是李白的作品的是？那么可以选6.4中值最小的......

如果眼睛快的话，看自动搜索的结果最准确，本来想把计算关联度那个弄得再准确点，结果发现很难。我现在答题还是老老实实看浏览器的自动搜索结果了，挺好用。
--------前段时间的例子--------
截图: 0.263000011444
ocr耗时: 0.898999929428
原问题: 五岳之一的泰山在我国的哪个省?
分词耗时: 0.0
选项: 山东 湖南 四川 
搜索: 五岳 泰山 我国 之一  中国 山东 湖南 四川
总耗时: 1.16199994087 秒
**推荐**
百度搜索
17	山东
14	四川
13	湖南

问答平台
13	山东
9	湖南
8	四川

参考-关联程度:
山东	1394
湖南	1367
四川	1332

★百度搜索
4	山东
3	湖南
0	四川

截图: 0.246999979019
ocr耗时: 0.979000091553
原问题: “绿蚁新醅酒,红泥小火炉”,这句诗中,此时的天气是怎样的?
分词耗时: 0.000999927520752
选项: 刚下完雪 正在下雪 快要下雪 
搜索: 红泥 绿蚁 火炉 这句 天气 怎样 此时  刚下完雪 正在下雪 快要下雪
总耗时: 1.22699999809 秒
**推荐**
百度搜索
8	快要下雪
8	正在下雪
7	刚下完雪

问答平台
319	刚下完雪
314	正在下雪
309	快要下雪

参考-关联程度:
快要下雪	34286
正在下雪	14967
刚下完雪	4926

★百度搜索
0	快要下雪
0	正在下雪
0	刚下完雪

截图: 0.25200009346
ocr耗时: 1.00699996948
原问题: 下列人物中,谁设计了现在的北大校徽的雏形?
分词耗时: 0.0
选项: 鲁迅 严复 陈独秀 
搜索: 校徽 雏形 北大 人物 设计 现在  鲁迅 严复 陈独秀
总耗时: 1.25999999046 秒
**推荐**
问答平台
9	鲁迅
4	严复
4	陈独秀

★百度搜索
20	鲁迅
0	严复
0	陈独秀

参考-关联程度:
鲁迅	7957
陈独秀	662
严复	10

百度搜索
35	鲁迅
22	陈独秀
12	严复
