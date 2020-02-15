#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 6 17:59:12 2020

@author: mac
"""

import jieba.analyse
import os
import csv

def is_uchar(uchar):
    """判断一个unicode是否是汉字"""
    if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
            return True
    """判断一个unicode是否是数字"""
    if uchar >= u'\u0030' and uchar<=u'\u0039':
            return True
    """判断一个unicode是否是英文字母"""
    if (uchar >= u'\u0041' and uchar<=u'\u005a') or (uchar >= u'\u0061' and uchar<=u'\u007a'):
            return True
    if uchar in (' '):
            return True
    return False

def get_keywords(text):
    """
    :param text: 评论文本
    :return: topic
    """
    #保留汉字、数字、英文和空格
    text = ''.join(list(filter(lambda x:is_uchar(x),list(text)))).strip()
    if(len(text)==0):
        return
    #选择词长范围为10~25的评论
    words = list(filter(lambda x: x!='',text.split(' ')))
    comments_length = len(words)
    if 10 < comments_length <= 50:

        top_k = int(comments_length // 5)

        #tf-idf 抽取关键词
        # keywords = list(jieba.analyse.extract_tags(text, topK=top_k, withWeight=False, allowPOS=()))
        '''
              sentence 需要提取的字符串，必须是str类型，不能是list
              topK 提取前多少个关键字
              withWeight 是否返回每个关键词的权重
              allowPOS是允许的提取的词性，默认为allowPOS空
        '''
        #tf-idf + 名词，动词，形容词 抽取关键词
        keywords2 = list(jieba.analyse.extract_tags(text, topK=top_k, allowPOS=(['n', 'v','a'])))
        #textrank + 名词，动词，形容词抽取关键词
        # keywords3 = list(jieba.analyse.textrank(text, topK=top_k, allowPOS=(['n', 'v','a'])))
        # print('动词，名次',keywords)

        return [comments_length, sort_keywords(keywords2,text).strip()]
    else:
        return

def sort_keywords(keywords,text):
    text_list = text.split(' ')
    keywords_list = keywords
    keywords_obj = {}
    topic = []

    # print(text_list)

    for keyword in keywords_list:  # 得到keywords 数组
        index = text_list.index(keyword)
        keywords_obj[keyword] = index

    # 这里对排序的规则进行了定义，x指元组，x[1]是值，x[0]是键
    for item in sorted(keywords_obj.items(), key=lambda x: x[1]):
        topic.append(item[0])

    return ' '.join(topic)

if __name__ == '__main__':
    root_path = '/home/shengyu/yeli/textGenerate/dataset'
    # root_path = '/Users/mac/workspace/textGenerate/dataset/'
    # root_path = r'A:\研三\textGenerate\dataset'
    file_path = os.path.join(root_path, 'movie_storyline_comment_similarity.csv')
    save_path = os.path.join(root_path, 'movie_storyline_comment_similarity_topic.csv')

    save_path_problem = os.path.join(root_path, 'movie_storyline_comment_similarity_topic_problem.csv')

    headers = ['MOVIE_ID', 'COMMENT', 'RATING', 'STORYLINE', 'TOPIC']


    with open(file_path, 'r',encoding='utf-8-sig') as f,open(save_path, 'w', newline='',encoding='utf-8-sig') as w,\
            open(save_path_problem, 'w', newline='',encoding='utf-8-sig') as wp:
        reader = csv.reader(f)
        print(type(reader))
        next(f)

        writer = csv.DictWriter(w, headers)
        writer.writeheader()

        writer_problem = csv.DictWriter(wp,['MOVIE_ID', 'COMMENT', 'RATING', 'STORYLINE'])
        writer_problem.writeheader()
        count = 0
        for row in reader:
            try:
                topic = get_keywords(row[1])
                if topic:
                    count += 1
                    rows = {'MOVIE_ID': row[0], 'COMMENT': row[1],'RATING': row[2], 'STORYLINE': row[3],
                         'TOPIC': topic[1]}
                    writer.writerow(rows)
            except ValueError:
                rows = {'MOVIE_ID': row[0], 'COMMENT': row[1], 'RATING': row[2], 'STORYLINE': row[3]}
                writer_problem.writerow(rows)
    print('总样例数:%d' % count)
    print('end')
