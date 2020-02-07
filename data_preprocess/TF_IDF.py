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
    def add_space(s):
        return ' '.join(list(s))

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


def write_csv(outfilename, headers, rows):  # 写入内容
    with open(outfilename, 'a', encoding='utf-8-sig')as f:
        f_csv = csv.DictWriter(f, headers)
        # 如果需要写入标题就可以
        f_csv.writerows(rows)
        f.close()

if __name__=='__main__':
    filename = "/home/shengyu/yeli/movie_storyline_comment.csv"
    outfilename = "/home/shengyu/yeli/textGenerate/dataset/movie_storyline_comment_topic_similarity.csv"

    # filename = '/Users/mac/Desktop/movie_storyline_comment.csv'
    # outfilename = '/Users/mac/Desktop/movie_storyline_comment_topic_similarity.csv'

    headers = ['MOVIE_ID', 'COMMENT', 'RATING', 'STORYLINE', 'TOPIC']
    with open(outfilename, 'a', encoding='utf-8-sig')as f0:  # 写入header
        f_csv = csv.DictWriter(f0, headers)
        f_csv.writeheader()

    with open(filename, 'r') as f:
        reader = csv.reader(f)
        print(type(reader))
        next(f)
        for row in reader:
            if len(row[1]) > 1:
                if len(row[3]) > 1:
                        if tfidf_similarity(row[1], row[3]) > 0.2:
                            rows = [{'MOVIE_ID': row[0], 'COMMENT': row[1], 'RATING': row[2], 'STORYLINE': row[3]}]
                            write_csv(outfilename, headers, rows)
                            print(rows)







