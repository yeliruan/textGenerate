#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 11:12:57 2020

@author: mac
"""
import numpy as np
import os
import pickle

if __name__=='__main__':
    
    cteg_root = '/Users/mac/Desktop/CTEG/data'
    my_root = '/Users/mac/workspace/textGenerate/data'

    word_dict = os.path.join(cteg_root,'word_dict_zhihu.npy')
    vocab_dict = np.load(word_dict).item()
    idx2word = {v: k for k, v in vocab_dict.items()}
    
    pretrain_wv = np.load(os.path.join(cteg_root,'wv_tencent.npy'))
    train_si = np.load(os.path.join(cteg_root,'train_src.npy'))
    train_src_len = np.load(os.path.join(cteg_root,'train_src_len.npy'))
    train_src_lbl_oh = np.load(os.path.join(cteg_root,'train_src_lbl_oh.npy'))
    f = open(os.path.join(cteg_root,'topic_list_100.pkl'),'rb')    
    topic_dict = pickle.load(f)
    train_mem_idx_120_concept = np.load(os.path.join(cteg_root,'train_mem_idx_120_concept.npy'))
    print(len(train_mem_idx_120_concept[0]))
    print(train_mem_idx_120_concept[20])
    print(train_si[20])
    print(idx2word[305])
    temp = ''
    for item in train_mem_idx_120_concept[20]:
        temp = temp + idx2word[item]
        temp = temp + ' '
    print(temp)   
    
    my_dict = open(os.path.join(my_root,'topic_new.pkl'),'rb')    
    my_topic_dict = pickle.load(my_dict)
    print(my_topic_dict)
    
    print(topic_dict)
    
    print(train_src_lbl_oh)
    
    print(train_src_len)
    print(train_src_len[15])
    
    print(train_si[15])
    print(idx2word[109],idx2word[527],idx2word[166])

    print(pretrain_wv)
    
    print(len(vocab_dict))
    
    my_word_dict = os.path.join(my_root,'word_dict.npy')
    vocab_dict = np.load(my_word_dict).item()
    print(len(vocab_dict))
    vocab_dict.pop('')
    
   
