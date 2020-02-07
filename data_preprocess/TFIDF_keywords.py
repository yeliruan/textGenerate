#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 6 17:59:12 2020

@author: mac
"""



import jieba.analyse
import codecs


def get_keywords(text):
    sentence = text
    print(text)

    '''
    sentence 需要提取的字符串，必须是str类型，不能是list
    topK 提取前多少个关键字
    withWeight 是否返回每个关键词的权重
    allowPOS是允许的提取的词性，默认为allowPOS=‘ns’, ‘n’, ‘vn’, ‘v’，提取地名、名词、动名词、动词
    '''

    keywords = "  ".join(jieba.analyse.extract_tags(sentence , topK=6, withWeight=False, allowPOS=()))

    # keywords = (jieba.analyse.extract_tags(sentence, topK=10, allowPOS=(['n', 'v','vn'])))
    # print('动词，名次',keywords)

    text_list = text.split(' ')
    keywords_list = keywords.split(' ')
    keywords_obj = {}
    topic = []

    for keyword in keywords_list:#得到keywords 数组
        index = text_list.index(keyword)
        keywords_obj[keyword] = index

    #这里对排序的规则进行了定义，x指元组，x[1]是值，x[0]是键
    for item in sorted(keywords_obj.items(),key=lambda x:x[1]):
        topic.append(item[0])

    print(topic)

    # print(sorted(keywords_obj.items(),key=lambda x:x[1]))

if __name__ == '__main__':
    file = r"/Users/mac/Desktop/test1.txt"
    text = codecs.open(file, 'r', 'utf-8').read()
    get_keywords(text)



