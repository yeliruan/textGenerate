#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:33:30 2019

@author: ruanyeli
"""


import jieba
import csv
import re

# 创建停用词列表
def stopwordslist():
    stopwords = [line.strip() for line in open('/Users/mac/Library/Mobile Documents/com~apple~CloudDocs/毕业论文代码/stopwords.txt',encoding='UTF-8').readlines()]
    return stopwords

# 对句子进行中文分词
def seg_depart(sentence):
    # 对文档中的每一行进行中文分词
    print("正在分词")
    sentence_depart = jieba.cut(sentence.strip())
    # 创建一个停用词列表
    stopwords = stopwordslist()
   
    # 输出结果为outstr
    outstr = ''
    # 去停用词
    for word in sentence_depart:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr

def write_csv(outfilename, headers, rows):
        with open(outfilename, 'a',encoding='utf-8-sig')as f:
            f_csv = csv.DictWriter(f, headers)
             # 如果需要写入标题就可以
            f_csv.writerows(rows)
            f.close()

# 给出文档路径
filename = "/Users/mac/Downloads/moviedata(total)/comments.csv"
outfilename = "/Users/mac/Desktop/movie_comment_jieba.csv"
#inputs = open(filename, 'r')
#outputs = open(outfilename, 'a+')

# 将输出结果写入ou.txt中
headers = ['MOVIE_ID', 'COMMENT','RATING']  
with open(outfilename, 'a',encoding='utf-8-sig')as f0:
            f_csv = csv.DictWriter(f0, headers)
            f_csv.writeheader() 

with open(filename, 'r') as f:
    reader = csv.reader(f)
    print(type(reader))
    for row in reader:
         line =re.sub('[a-zA-Z0-9\n]','',row[3])
         line_seg = seg_depart(line)
         if len(line_seg)>=len(row[2]):
             rows = [{'MOVIE_ID':row[2], 'COMMENT':line_seg, 'RATING':row[6]}]
         else:
             rows = [{'MOVIE_ID':line_seg, 'STORYLINE':row[2], 'RATING':row[6]}]
         print(rows)
         if len(line_seg) > 35:
            write_csv(outfilename, headers, rows) 
    
#outputs.close()
#inputs.close()
print("删除停用词和分词成功！！！")