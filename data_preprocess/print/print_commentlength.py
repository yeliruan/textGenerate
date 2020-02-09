#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 17:59:12 2020

@author: mac
"""

import csv

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

import seaborn as sns
import os

def handle_commentlength_print(origin_file, imgsave_path):
    with open(origin_file, 'r', encoding="utf-8") as f:
        reader = csv.reader(f)
        print(type(reader))

        # 统计评论长度
        # 绘制直方图
        # 选取max_length

        comments_length_list = []
        count = 0
        maxlength = 0

        for row in reader:
            count += 1
            comments_length = len(list(row[3]))
            if comments_length > maxlength:
                maxlength = comments_length

            comments_length_list.append(comments_length)
        group = []
        print(maxlength)

        for i in range(200):
            group.append(i)
        # sns.set_palette("hls") #设置所有图的颜色，使用hls色彩空间
        # sns.distplot(storyline_length,color="b",bins=30,kde=True)

        plt.hist(comments_length_list, group, histtype='bar', rwidth=0.8)
        plt.legend()

        plt.xlabel('comments_length_group')
        plt.ylabel('number')
        # plt.title('测试例子——直方图')
        plt.savefig(imgsave_path)
        plt.show()



if __name__ == '__main__':
    # root_path = '/Users/mac/Desktop/'
    root_path = '/home/shengyu/yeli/textGenerate/dataset/moviedata'

    origin_file = os.path.join(root_path, 'comments.csv')#原始comments
    imgsave_path = os.path.join(root_path, 'comments_length.jpg')

    handle_commentlength_print(origin_file, imgsave_path)
