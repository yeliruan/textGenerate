#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 19:23:55 2020

@author: mac
"""

from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import os

def checkfile(file,writer):
    
    try:
        model = Word2Vec(LineSentence(file),size=300,window=5,min_count=1,workers=4,sg=1)
        print('---')
    except:
        print('fiie is ',file)
        writer.write(file+'\n')


if __name__=='__main__':
#    root_dir = '/home/shengyu/yeli/textGenerate/dataset'
 #   save_path = 'home/shengyu/yeli/textGenerate/test.txt'
    root_dir = '/Users/mac/workspace/textGenerate/dataset/comments'
    save_path = '/Users/mac/workspace/textGenerate/test.txt'
    writer = open(save_path,'w',encoding='utf8')
    for file_name in os.listdir(root_dir):
        checkfile(os.path.join(root_dir,file_name),writer)
    #model = Word2Vec(LineSentence(os.path.join(root_dir,'c_2080238.txt')),size=300,window=5,min_count=1,workers=4,sg=1)
    writer.close()
    print('end')