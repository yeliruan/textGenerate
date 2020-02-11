#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 16:59:29 2020

@author: mac
@desc:将样例中topic空白样例去掉
剔除topic中的低频词
"""

import csv
import pickle
import os

def handle(origin_path,new_file_path,topics_list_save_path,low_thredshod):
    '''origin _path:样例文件地址'''
    '''save_path:生成更新样例文件和topic词list保存地址'''
    '''low_thredshod:topic低频保留阈值'''

    #保存低频topic词和高频词
    low_topics = set()
    high_topics = set()

    with open(origin_path, 'r',encoding='utf8') as f:
        reader = csv.reader(f)
        print(type(reader))
        next(f)

        # 处理低频topic词
        # 统计topic频数
        # 保存topic词-频数
        topic_dict = dict()
        for row in reader:
            #去除topic为空的样例
            if(row[4].strip()==''):
                continue

            topics = row[4].split(' ')
            for topic in topics:
                if(topic == ''):
                    continue
                if topic in topic_dict:
                    topic_dict[topic] = topic_dict[topic] + 1
                else:
                    topic_dict[topic] = 1

                #区分高低频词
            for topic in topic_dict:
                if(topic_dict[topic]>=low_thredshod):
                    high_topics.add(topic)
                else:
                    low_topics.add(topic)

    #剔除低频词,并把新的样例写入new_file


    header = ['MOVIE_ID', 'COMMENT','RATING','SROTYLINE','TOPIC']

    with open(origin_path, 'r',encoding='utf8') as f,open(new_file_path,'a',encoding='utf8') as w:
        reader = csv.reader(f)
        print(type(reader))
        next(f)

        f_csv = csv.DictWriter(w, header)
        # 写入标题
        f_csv.writeheader()

        for row in reader:
            #去除comment中的空字符
            comment_words = row[1].split(' ')
            new_row_1 = []
            for comment_word in comment_words:
                if(comment_word!=''):
                    new_row_1.append(comment_word)
            row[1] = ' '.join(new_row_1)

            #去除简介中的空字符
            storyline_words = row[3].split(' ')
            new_row_3 = []
            for storyline_word in storyline_words:
                if(storyline_word!=''):
                    new_row_3.append(storyline_word)
            row[3] = ' '.join(new_row_3)

            #去除低频词和空字符
            topics = row[4].split(' ')
            new_topics = []
            for topic in topics:
                if(topic in high_topics):
                    new_topics.append(topic)
            if(len(new_topics)>0):
                row[4] = ' '.join(new_topics)
                rows = [{'MOVIE_ID': row[0], 'COMMENT': row[1], 'RATING': row[2], 'SROTYLINE': row[3], 'TOPIC': row[4]}]
                f_csv.writerows(rows)


    #写入topic list
    with open(topics_list_save_path,'w',encoding='utf8') as w:
        w.write(' '.join(high_topics))

if __name__=='__main__':
    root_path = '/home/shengyu/yeli/textGenerate/dataset'
    #root_path = r'A:\研三\textGenerate\dataset'
    inputfile = os.path.join(root_path,'movie_storyline_comment_topic_similarity_topic.csv')
    inputfile_new = os.path.join(root_path,'movie_storyline_comment_topic_similarity_topic_new.csv')
    save_path = os.path.join(root_path,'topic_new.txt')
    handle(inputfile,inputfile_new,save_path,2)
    print('end')


def write_csv(outfilename, headers, rows):
    with open(outfilename, 'a',encoding='utf-8-sig')as f:
        f_csv = csv.DictWriter(f, headers)
                 # 如果需要写入标题就可以
        f_csv.writerows(rows)
