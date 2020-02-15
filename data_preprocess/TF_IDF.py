#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 21:17:19 2020

@author: mac
"""

from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from scipy.linalg import norm
import csv


def tfidf_similarity(s1, s2):
    """
    :param s1: 句子1
    :param s2: 句子2
    :return: 两个句子的相似值
    """
    # 将字中间加入空格
    s1, s2 = add_space(s1), add_space(s2)
    # 转化为TF矩阵
    cv = TfidfVectorizer(tokenizer=lambda s: s.split())
    corpus = [s1, s2]
    vectors = cv.fit_transform(corpus).toarray()
    # 计算TF系数
    if (norm(vectors[0]) * norm(vectors[1])) == 0:
        return 0
    return np.dot(vectors[0], vectors[1]) / (norm(vectors[0]) * norm(vectors[1]))


def add_space(s):
    return ' '.join(list(s))


def write_csv(outfilename, headers, rows):  # 写入内容
    with open(outfilename, 'a', encoding='utf8')as f:
        f_csv = csv.DictWriter(f, headers)
        # 如果需要写入标题就可以
        f_csv.writerows(rows)
        f.close()

if __name__=='__main__':
    filename = "/home/shengyu/yeli/movie_storyline_comment.csv"
    outfilename = "/home/shengyu/yeli/textGenerate/dataset/movie_storyline_comment_similarity.csv"

    # filename = '/Users/mac/Desktop/movie_storyline_comment.csv'
    # outfilename = '/Users/mac/Desktop/movie_storyline_comment_topic_similarity.csv'

    # filename = r'A:\研三\textGenerate\dataset\movie_storyline_comment.csv'
    # outfilename = r'A:\研三\textGenerate\dataset\movie_storyline_comment_similarity.csv'

    #02.15 增加similarity列，评论和简介的相似度，用于筛选样例
    # 阅读数据发现，评论和简介存在直接粘贴复制的情况，因此给相似度设置一个最高阈值0.66
    headers = ['MOVIE_ID', 'COMMENT', 'RATING', 'STORYLINE','SIMILARITY']

    with open(filename, 'r',encoding='utf8') as f,open(outfilename, 'w',newline='', encoding='utf-8-sig')as w:
        reader = csv.reader(f)
        # 写入header
        writer = csv.DictWriter(w, headers)
        writer.writeheader()
        print(type(reader))
        next(f)
        count = 0
        
        for row in reader:
            if len(row[1]) > 1:
                if len(row[3]) > 1:
                    try:
                        similarity = tfidf_similarity(row[1],row[3])
                        if similarity > 0.3 and similarity <0.66:
                            rows = [{'MOVIE_ID': row[0], 'COMMENT': row[1], 'RATING': row[2], 'STORYLINE': row[3],'SIMILARITY':similarity}]
                            # 如果需要写入标题就可以
                            writer.writerows(rows)
                            count += 1
                            # print(rows)
                    except:
                        print('这条评论有问题', 'ID: ', row[0], 'COMMENT: ', row[1])

    print(count)






