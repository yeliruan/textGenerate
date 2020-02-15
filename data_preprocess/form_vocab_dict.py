#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__doc__ = 'description'
__author__ = '13314409603@163.com'

import os
from gensim.models import Word2Vec
import csv
import numpy as np
from util import constant

def get_vocab_dict(input_file_path,word_frequency_save_path,thredshod,vocab_dict_save_path,word2vec_path,pretrain_wv_save_path):
    vocab_dict = dict()

    with open(input_file_path,'r',encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        print(type(reader))
        next(f)

        for row in reader:
            for word in row[1].split(' '):
                if(word in vocab_dict):
                    vocab_dict[word] += 1
                else:
                    vocab_dict[word] = 1
            for word in row[3].split(' '):
                if (word in vocab_dict):
                    vocab_dict[word] += 1
                else:
                    vocab_dict[word] = 1

    sorted_vocab = sorted(vocab_dict.items(), key=lambda x: x[1])
    print('词典长度',len(vocab_dict))

    #把所有的词和词频保存
    with open(word_frequency_save_path,'w',newline='',encoding='utf-8-sig') as w:
        f_csv = csv.DictWriter(w, ['word','FREQUENCY'])
        # 写入标题
        f_csv.writeheader()
        for item in sorted_vocab:
            f_csv.writerow({'word':item[0],'FREQUENCY':item[1]})

    #按照最低阈值，去除低频词

    new_vocab_dict = {}
    pretrain_wv = []
    index = 0
    # 加入特殊符号
    print('word2vec load from ' + word2vec_path)
    model = Word2Vec.load(word2vec_path)
    wv = model.wv
    new_vocab_dict[constant.PAD_TAG] = index
    pretrain_wv.append(np.zeros(wv.vector_size))

    index += 1
    new_vocab_dict[constant.UNKNOW_TAG] = index
    pretrain_wv.append(np.random.rand(wv.vector_size))

    index += 1
    new_vocab_dict[constant.BEGIN_TAG] = index
    pretrain_wv.append(np.random.rand(wv.vector_size))

    index += 1
    new_vocab_dict[constant.END_TAG] = index
    pretrain_wv.append(np.random.rand(wv.vector_size))


    for item in vocab_dict.items():
        if(item[1]>=thredshod):
            try:
                pretrain_wv.append(wv[item[0]])
                new_vocab_dict[item[0]] = index
                index +=1
            except:
                continue


    np.save(vocab_dict_save_path,new_vocab_dict)
    np.save(pretrain_wv_save_path,pretrain_wv)


if __name__ == '__main__':

    # root_path = r'A:\研三\textGenerate'
    root_path = '/home/shengyu/yeli/textGenerate/dataset'

    dataset_path = os.path.join(root_path,'dataset')

    input_file_path = os.path.join(dataset_path,'movie_storyline_comment_similarity_topic_new.csv')
    word2vec_path = os.path.join(os.path.join(root_path,'word2vec'),'word2vec_model')

    word_frequency_save_path = os.path.join(dataset_path,'words_frequency.csv')
    vocab_dict_save_path = os.path.join(dataset_path,'vocab_dict.npy')
    pretrain_wv_save_path = os.path.join(dataset_path,'wv_tencent.npy')
    get_vocab_dict(input_file_path,word_frequency_save_path,1,vocab_dict_save_path,word2vec_path,pretrain_wv_save_path)