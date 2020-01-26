
__doc__ = 'description' \
          '统计简介长度并画图'
__author__ = 'ruanyeli'


import csv

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

import os


def handle_print(origin_file):

    with open(origin_file, 'r',encoding='utf8') as f:
        reader = csv.reader(f)
        print(type(reader))
        
        next(f)
        # 统计简介长度
        # 绘制直方图
        # 选取max_length

        storyline_length = []

        for row in reader:
            storyline = row[4].split(' ')
            storyline_length.append(len(storyline))

    group = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
    
    plt.hist(storyline_length, group, histtype='bar', rwidth=0.8)
    plt.legend()

    plt.xlabel('storyline_length-group')
    plt.ylabel('storyline_length')
    plt.title(u'测试例子——直方图')
    
    plt.show()
    

if __name__ == '__main__':
    root_path = '/Users/mac/Desktop/'
    #root_path = '/home/shengyu/yeli/textGenerate/dataset'

    origin_file = os.path.join(root_path,'movie_storyline_comment_topic_fuwu.csv')
    
    handle_print(origin_file)

    

    