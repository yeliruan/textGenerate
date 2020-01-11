#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 11:56:36 2020

@author: mac
"""

from gensim.models import Word2Vec
from gensim.models.word2vec import PathLineSentences
import os


def train(root_dir,dataset_path):
    print('word2vec begin to train')
    print('load dataset at '+ dataset_path)
    model = Word2Vec(PathLineSentences(dataset_path,enconding='gbk'),size=300,window=5,min_count=1,workers=4,sg=1)
    print('word2vec train end')
    print('word2vec model save to '+save_path)
    model.save(save_path)
    

def test(model_save_path): 
    print('word2vec load from '+model_save_path)
    model = Word2Vec.load(model_save_path)
    wv = model.wv
    print(wv['爱情'])
    print(wv.most_similar('爱情'))
    

if __name__=='__main__':
    #this path is in my mac
    #root_dir = r'/Users/mac/workspace/textGenerate'
    #this path is in linux server
    root_dir = r'/home/shengyu/yeli/textGenerate/'
    dataset_path = os.path.join(root_dir,'dataset/comments')
    save_path = os.path.join(root_dir,'word2vec_model')
    train(dataset_path,save_path)
    test(save_path)
    print('end')
    