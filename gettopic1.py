#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 16:59:29 2020

@author: mac
"""

import csv
import pickle

def write_csv(outfilename, headers, rows):
    with open(outfilename, 'a',encoding='utf-8-sig')as f:
        f_csv = csv.DictWriter(f, headers)
                 # 如果需要写入标题就可以
        f_csv.writerows(rows)
        f.close() 


if __name__=='__main__':
    inputfile = '/home/shengyu/yeli/movie_storyline_comment_topic.csv'
    inputfile_new ='/home/shengyu/yeli/movie_storyline_comment_topic_new.csv'
    save_path = '/home/shengyu/yeli/textGenerate/topic.txt'
    dict_save_path = '/home/shengyu/yeli/textGenerate/topic_dict.pkl'
    movie_storyline_comment_topic_new = '/home/shengyu/yeli/movie_storyline_comment_topic_new.csv'
    
    
    topic_set = set()
    topic_dict = {}
    topic_dict_delete = {}
    
    headers = ['MOVIE_ID', 'COMMENT','RATING','SROTYLINE','TOPIC'] 
    
    with open(inputfile, 'r',encoding='utf8') as f: #topic 长度大于0的另存为
        reader = csv.reader(f)
        print(type(reader))
        next(f)
        for row in reader:
            rows = row[4].split(' ')
            if len(rows) > 0 :
                rows = [{'MOVIE_ID':row[0], 'COMMENT':row[1], 'RATING':row[2],'SROTYLINE':row[3],'TOPIC':row[4]}]
                topic_rows = row[4].split(' ')
                for rowitem in rows:
                    if rowitem in topic_dict:
                        topic_dict[rowitem] = topic_dict[rowitem]+1
                    else:
                        topic_dict[rowitem] = 1
                write_csv(inputfile_new,headers,rows)           
                    

    for key in topic_dict:
        if topic_dict[key] > 1:
            topic_set.add(key)
        else:
            topic_dict_delete[key] = key    
                    
    with open(inputfile_new, 'r',encoding='utf8') as f,open(movie_storyline_comment_topic_new, 'r',encoding='utf8') as f1:
         f_csv = csv.DictWriter(f1, headers)
         f_csv.writeheader() 
         reader = csv.reader(f)
         print(type(reader))
         next(f)
         for row in reader:
             topic_rows = row[4].split(' ')
             topic_new = ''
             for rowitem in topic_rows: 
                 if rowitem not in topic_dict_delete:
                     topic_new = topic_new + rowitem 
                     topic_new = topic_new + ' '
             rows = [{'MOVIE_ID':row[0], 'COMMENT':row[1], 'RATING':row[2],'SROTYLINE':row[3],'TOPIC':topic_new}]
             write_csv(movie_storyline_comment_topic_new,headers,rows)
   
    
    with open(dict_save_path, 'wb') as fo:     # 将数据写入pkl文件
        pickle.dump(topic_dict, fo)
       
          
    with open(save_path, 'w') as fo:     # 将数据写入pkl文件
        fo.write(topic_set)




   
            
            
    

            
            