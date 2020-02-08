#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 8 02:32:12 2020

@author: mac
"""


import csv
import matplotlib.pyplot as plt
import os


def handle_score_print(origin_file, imgsave_path):
    with open(origin_file, 'r', encoding="utf-8") as f:
        reader = csv.reader(f)
        print(type(reader))
        next(f)

        # 统计评论长度
        # 绘制直方图
        # 选取max_length

        score_list = []
        count = 0

        for row in reader:
            if row[2]!='':
                count += 1
                print(int(row[2]))
                score_list.append(int(row[2]))

        group = [0,1,2,3,4,5]
        print(score_list)
        print('count',count)

        # sns.set_palette("hls") #设置所有图的颜色，使用hls色彩空间
        # sns.distplot(storyline_length,color="b",bins=30,kde=True)

        plt.plot(group, score_list, linewidth=5, color='b')  # 将列表传递给plot,并设置线宽，设置颜色，默认为蓝色
        plt.xlabel("score_group", fontsize=14, color='g')  # 设置轴标题，并给定字号,设置颜色
        plt.ylabel("Squares Of Value", fontsize=14, color='g')
        plt.tick_params(axis='both', labelsize=14)  # 设置刻度标记的大小
        plt.savefig(imgsave_path)
        plt.show()  # 显示


if __name__ == '__main__':
    # root_path = '/Users/mac/Desktop/'
    root_path = '/home/shengyu/yeli/textGenerate/dataset/moviedata'
    save_path = '/home/shengyu/yeli/textGenerate/dataset/score_length_zhexian.jpg'

    origin_file = os.path.join(root_path, 'comments.csv')#原始comments
    handle_score_print(origin_file, save_path)
