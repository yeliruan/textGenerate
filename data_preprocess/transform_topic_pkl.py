#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 5 18:12:57 2020

@author: ruanyeli
"""
import numpy as np
import os
import pickle

if __name__=='__main__':

    origin_path = '/home/shengyu/yeli/textGenerate/dataset/topic_new.txt'
    save_path = '/home/shengyu/yeli/textGenerate/dataset/cteg/topic_list_100.pkl'

    # origin_path = '/Users/mac/Desktop/topic_new.txt'
    # save_path = '/Users/mac/Desktop/topic_list_100.pkl'

    # origin_path = r'A:\研三\textGenerate\dataset\topic_new.txt'
    # save_path = r'A:\研三\textGenerate\dataset\topic_list_100.pkl'

    topic = []
    with open(origin_path, "r",encoding='utf8') as f,open(save_path, "wb") as w:  # 打开文件
        data = f.read()  # 读取文件
        data = data.split(" ")

        pickle.dump(data, w)

    f = open(save_path, 'rb')
    topic_dict = pickle.load(f)
    print(topic_dict)

