# -*- coding: utf-8 -*-
#future是把下一个新版本的特性导入到当前版本，于是我们就可以在当前版本中测试一些新版本的特性
from __future__ import print_function
from __future__ import unicode_literals

from snownlp import normal#文字转换成拼音
from snownlp import seg#中文分词
from snownlp.summary import textrank#提取文本摘要，提取关键词


if __name__ == '__main__':#如果当前模块为主模块，则执行“main”/如果模块是被导入，_name_的值为模块名字，如果模块是被直接执行，_name_的值为"main"
    t = normal.zh2hans(text)#zh2hans繁体字和简体字互相转换
    sents = normal.get_sentences(t)
    doc = []
    for sent in sents:
        words = seg.seg(sent)
        words = normal.filter_stop(words)
        doc.append(words)
    rank = textrank.TextRank(doc)
    rank.solve()
    for index in rank.top_index(5):
        print(sents[index])
    keyword_rank = textrank.KeywordTextRank(doc)
    keyword_rank.solve()
    for w in keyword_rank.top_index(5):
        print(w)
