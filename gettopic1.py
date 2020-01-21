#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 16:59:29 2020

@author: mac
"""

import csv
import pickle

if __name__=='__main__':
    inputfile = '/home/shengyu/yeli/movie_storyline_comment_topic.csv'
    save_path = '/home/shengyu/yeli/textGenerate/topic.txt'
    dict_save_path = '/home/shengyu/yeli/textGenerate/topic_dict.pkl'

    topic_set = set()
    topic_dict = {}
    topic_dict_delete = {}
    
    with open(inputfile, 'r',encoding='utf8') as f:
        reader = csv.reader(f)
        print(type(reader))
        next(f)
        for row in reader:
            rows = row[4].split(' ')
            for rowitem in rows:
                if rowitem in topic_dict:
                    topic_dict[rowitem] = topic_dict[rowitem]+1
                else:
                    topic_dict[rowitem] = 1
    
    for key in topic_dict:
        if topic_dict[key] >1:
            topic_set.add(key)
        else:
            
            
            
    print(topic_set)  

    with open(dict_save_path, 'wb') as fo:     # 将数据写入pkl文件
        pickle.dump(topic_dict, fo)
       
          
    with open(save_path, 'w') as fo:     # 将数据写入pkl文件
        fo.write(topic_set)

            
            
    

            
            