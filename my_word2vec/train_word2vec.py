#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 11:56:36 2020

@author: mac
"""

from gensim.models import Word2Vec
from gensim.models.word2vec import PathLineSentences
import os
import numpy as np


def train(dataset_path,save_path):
    print('word2vec begin to train')
    print('load dataset at '+ dataset_path)
    model = Word2Vec(PathLineSentences(dataset_path),size=200,window=5,min_count=2,workers=4,sg=1)
    print('word2vec train end')
    print('word2vec model save to '+save_path)
    model.save(save_path)
    

def test(model_save_path): 
    print('word2vec load from '+model_save_path)
    model = Word2Vec.load(model_save_path)
    wv = model.wv
    print(wv['爱情'])
    print(wv.most_similar('爱情'))

def get_vocab_dict(model_save_path,vocab_dict_save_path):
    print('word2vec load from '+model_save_path)
    model = Word2Vec.load(model_save_path)
    wv = model.wv
    wv['<PAD>'] = np.zeros(wv.vector_size)
    wv['<GO>'] = np.zeros(wv.vector_size)
    wv['<UNK>'] = np.zeros(wv.vector_size)
    wv['<EOS>'] = np.zeros(wv.vector_size)

    vocab_dict = dict()
    index = 0
    for key in model.wv.vocab.keys() :
        vocab_dict[key] = index
        index+=1

    np.save(vocab_dict_save_path,vocab_dict )
    print('词典长度',len(vocab_dict))

if __name__=='__main__':
    #this path is in my mac
    #root_dir = r'/Users/mac/workspace/textGenerate'

    #this path is in linux server
    root_dir = '/home/shengyu/yeli/textGenerate/'

    #this path is in windows
    #root_dir = r'A:\研三\textGenerate'

    #用来存储训练word2vec的所有文件
    dataset_path = os.path.join(os.path.join(root_dir,'dataset'),'word2vec_train_dataset')
    #用来存储word2vec的训练结果模型
    word2vec_dir = os.path.join(root_dir,'word2vec')
    save_path = os.path.join(word2vec_dir,'word2vec_model')
    vocab_dict_save_path = os.path.join(os.path.join(root_dir,'dataset'),'vocab_dict.npy')

    #train(dataset_path,save_path)
    # test(save_path)
    get_vocab_dict(save_path,vocab_dict_save_path)
    print('end')
    
