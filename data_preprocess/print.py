#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 17:59:12 2020

@author: mac
"""


import csv

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

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

    plt.hist(storyline_length, group, histtype='bar', rwidth=0.8)
    plt.legend()

    plt.xlabel('storyline_length-group')
    plt.ylabel('storyline_length')
    plt.title('测试例子——直方图')
    
    plt.savefig(imgsave_path)    
    plt.show()
    
if __name__ == '__main__':
    #root_path = '/Users/mac/Desktop/'
    root_path = '/home/shengyu/yeli/textGenerate/dataset'
    
    
    origin_file = os.path.join(root_path,'movie_storyline_comment_topic_new.csv')
    imgsave_path = os.path.join(root_path,'storyline_length.jpg')
    
    handle_print(origin_file,imgsave_path)
