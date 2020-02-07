#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 8 02:32:12 2020

@author: mac
"""

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
                score_list.append(int(row[2]))

        group = [0,1,2,3,4,5]
        print(score_list)
        print('count',count)

        # sns.set_palette("hls") #设置所有图的颜色，使用hls色彩空间
        # sns.distplot(storyline_length,color="b",bins=30,kde=True)

        plt.hist(score_list, group, histtype='bar', rwidth=0.8)
        plt.legend()

        plt.xlabel('score_group')
        plt.ylabel('number')
        # plt.title('测试例子——直方图')
        plt.savefig(imgsave_path)
        plt.show()

if __name__ == '__main__':
    # root_path = '/Users/mac/Desktop/'
    root_path = '/home/shengyu/yeli/textGenerate/dataset/moviedata'
    save_path = '/home/shengyu/yeli/textGenerate/dataset/score_length.jpg'

    origin_file = os.path.join(root_path, 'comments.csv')#原始comments
    handle_score_print(origin_file, save_path)
