#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 15:27:05 2020

@author: mac
"""
import csv
import numpy as np


def write_csv(outfilename, headers, rows):
        with open(outfilename, 'a',encoding='utf-8-sig')as f:
            f_csv = csv.DictWriter(f, headers)
             # 如果需要写入标题就可以
            f_csv.writerows(rows)
            f.close()
            

filename = "/home/shengyu/yeli/textGenerate/dataset/movie_storyline_comment_topic_new.csv" #得到电影简介
outfilename = "/home/shengyu/yeli/textGenerate/dataset/topic_small.csv"

headers = ['MOVIE_ID', 'COMMENT','RATING','SROTYLINE','TOPIC'] 


with open(filename, 'r') as f:
    reader = csv.reader(f)
    count = 0
    next(f)
    for row in reader:
         count = count+1
         if count <= 50000:
             rows = [{'MOVIE_ID':row[0], 'COMMENT':row[1], 'RATING':row[2],'SROTYLINE':row[3],'TOPIC':row[4]}]
             print(rows)
             write_csv(outfilename, headers, rows)
        






