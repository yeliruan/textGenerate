#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 17:59:12 2020

@author: mac
"""


import csv

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
#
import seaborn as sns
import os

def handle_print(origin_file,imgsave_path):

    with open(origin_file, 'r',encoding="utf-8") as f:
        reader = csv.reader(f)
        print(type(reader))

        # 统计简介长度
        # 绘制直方图
        # 选取max_length

        storyline_length = []
        count = 0
        maxlength = 0

        for row in reader:
            count = count+1
            storyline = row[3].split(' ')
            if len(storyline) > maxlength:
                maxlength = len(storyline)
            storyline_length.append(len(storyline))


    group = []
    for i in range(maxlength+1):
        group.append(i)

    # sns.set_palette("hls") #设置所有图的颜色，使用hls色彩空间
    # sns.distplot(storyline_length,color="b",bins=30,kde=True)


    plt.hist(storyline_length, group, histtype='bar', rwidth=0.8)
    plt.legend()

    plt.xlabel('storyline_length_group')
    plt.ylabel('number')
    #plt.title('测试例子——直方图')
    plt.savefig(imgsave_path)
    plt.show()
    

def cal_sentence_length(origin_file,rate):
    max_length = 4000 #假设句子一定小于这个值
    with open(origin_file, 'r', encoding="utf-8") as f:
        reader = csv.reader(f)
        print(type(reader))

        #统计各个长度（索引）句子的个数,初始化每个长度的句子个数都为0
        lengths_value = [0 for _ in range(max_length)]

        for row in reader:
            storyline = row[3].split(' ')
            the_length = len(storyline)
            lengths_value[the_length] += 1

    #统计长度小于某个值（索引）的句子总数
    sums =[0 for _ in range(max_length)]
    sum = 0
    for index,value in enumerate(lengths_value):
        sum+=value
        sums[index] = sum

    #求小于某个句长threshold的句子占比为rate
    for index in range(max_length):
        if(sums[index]/sums[-1]>=rate):
            print(index)
            return index


if __name__ == '__main__':
    #root_path = '/Users/mac/Desktop/'
    # root_path = r'A:\研三\textGenerate\dataset'
    root_path = '/home/shengyu/yeli/textGenerate/dataset'
    
    
    origin_file = os.path.join(root_path,'movie_storyline_comment_similarity_topic_new.csv')
    imgsave_path = os.path.join(root_path,'storyline_length.jpg')
    
    # handle_print(origin_file,imgsave_path)
    cal_sentence_length(origin_file,0.95)
