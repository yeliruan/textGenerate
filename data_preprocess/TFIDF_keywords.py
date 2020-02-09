#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 6 17:59:12 2020

@author: mac
"""

import jieba.analyse
import os
import csv


def get_keywords(text):
    """
    :param text: 评论文本
    :return: topic
    """

    comments_length = len(list(text))

    if 20 < comments_length < 100:

        top_k = int(comments_length // 10)
        keywords = "  ".join(jieba.analyse.extract_tags(text, topK=top_k, withWeight=False, allowPOS=()))
        '''
              sentence 需要提取的字符串，必须是str类型，不能是list
              topK 提取前多少个关键字
              withWeight 是否返回每个关键词的权重
              allowPOS是允许的提取的词性，默认为allowPOS=‘ns’, ‘n’, ‘vn’, ‘v’，提取地名、名词、动名词、动词
        '''

        # keywords = (jieba.analyse.extract_tags(sentence, topK=10, allowPOS=(['n', 'v','vn'])))
        # print('动词，名次',keywords)

        text_list = text.split(' ')
        keywords_list = keywords.split(' ')
        keywords_obj = {}
        topic = []

        # print(text_list)

        for keyword in keywords_list:  # 得到keywords 数组
            index = text_list.index(keyword)
            keywords_obj[keyword] = index

        # 这里对排序的规则进行了定义，x指元组，x[1]是值，x[0]是键
        for item in sorted(keywords_obj.items(), key=lambda x: x[1]):
            topic.append(item[0])

        topic_str = ''

        for topic_item in topic:
            if topic_item != '':
                topic_str = topic_str + topic_item + ' '

        return [comments_length, topic_str.strip()]
    else:
        return


def write_csv(savefile, headers, rows):  # 写入内容
    with open(savefile, 'a', encoding='utf-8-sig')as f:
        f_csv = csv.DictWriter(f, headers)
        # 如果需要写入标题就可以
        f_csv.writerows(rows)


if __name__ == '__main__':
    root_path = '/home/shengyu/yeli/textGenerate/dataset'
    # root_path = '/Users/mac/workspace/textGenerate/dataset/'
    file_path = os.path.join(root_path, 'movie_storyline_comment_topic_similarity.csv')
    save_path = os.path.join(root_path, 'movie_storyline_comment_topic_similarity_topic.csv')

    save_path_problem = os.path.join(root_path, 'movie_storyline_comment_topic_similarity_topic_problem.csv')

    headers = ['MOVIE_ID', 'COMMENT', 'RATING', 'STORYLINE', 'TOPIC']

    with open(save_path, 'a', encoding='utf-8-sig') as w:  # 写入header
        f_csv = csv.DictWriter(w, headers)
        f_csv.writeheader()

    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        print(type(reader))
        next(f)
        count = 0
        for row in reader:
            try:
                topic = get_keywords(row[1])
                if topic:
                    count += 1
                    rows = [
                        {'MOVIE_ID': row[0], 'COMMENT': row[1], 'RATING': row[2], 'STORYLINE': row[3],
                         'TOPIC': topic[1]}]
                    write_csv(save_path, headers, rows)
            except ValueError:
                rows = [{'MOVIE_ID': row[0], 'COMMENT': row[1], 'RATING': row[2], 'STORYLINE': row[3]}]
                write_csv(save_path_problem, ['MOVIE_ID', 'COMMENT', 'RATING', 'STORYLINE'], rows)

    print('end')
