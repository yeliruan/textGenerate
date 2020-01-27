#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__doc__ = 'description' \
          '将movie_storyline_comment_topic.csv初始样例转换为CTEG输入数据格式'
__author__ = '13314409603@163.com'

import csv
import numpy as np
from util.constant import PAD_TAG
from util.constant import TRAIN_TEST_VAL
import os

def handle(origin_file,vocab_dict,topic_list,save_path,backgroud_knowledge_max_length=168):

    '''origin file 格式：movie_id  comment rating  storyline   topic'''
    '''movie_id:电影id'''
    '''comment: 评论，已分词，空格间隔'''
    '''rating: 分数0~5'''
    '''storyline：简介，已分词，空格间隔'''
    '''topic:候选主题列表，空格分割'''

    '''vocab_dict:字典-word-id'''
    '''topic_list:主题集'''
    '''backgroud_knowledge_max_length:背景知识最大长度'''
    '''save_path:生成文件保存路径'''

    topic_examples = []
    topic_lens = []
    topic_identifiers = []
    comment_examples = []
    comment_lens = []
    mem = []

    with open(origin_file, 'r',encoding='utf8') as f:
        reader = csv.reader(f)
        #去掉第一行header
        next(f)

        for row in reader:
            movie_id = row[0]
            comment_str = row[1]
            rating_str = row[2]
            storyline_str = row[3]
            topic_str = row[4]

            topics = topic_str.split(' ')
            for topic in topics:
                print(topic)
                print(vocab_dict[topic])            
            topic_examples.append([vocab_dict[topic] for topic in topics])
            topic_lens.append(len(topics))
            topic_identifiers.append([1 if topic in topics else 0 for topic in topic_list])

            comment_words = comment_str.split(' ')
            comment_examples.append([vocab_dict[word] for word in comment_words])
            comment_lens.append(len(comment_words))

            storyline_words = storyline_str.splie(' ')

            #将简介填充或截取
            if(len(storyline_words)>backgroud_knowledge_max_length):
                storyline_words = storyline_words[0:backgroud_knowledge_max_length]
            else:
                storyline_words.extends[[PAD_TAG for i in range(backgroud_knowledge_max_length-len(storyline_words))]]
            assert len(storyline_words==backgroud_knowledge_max_length)

            #简介word转id
            mem.append([vocab_dict[word] for word in storyline_words])

    #训练：测试：评估分段
    assert TRAIN_TEST_VAL[0]+TRAIN_TEST_VAL[1]+TRAIN_TEST_VAL[2]==1
    total_examples_length = len(topic_examples)
    train_threshold = TRAIN_TEST_VAL[0]*total_examples_length
    test_threshold = TRAIN_TEST_VAL[1]*total_examples_length+train_threshold

    #训练数据
    #si_train 话题
    si_train_path = os.path.join(save_path,'train_src.npy')
    np.save(si_train_path,topic_examples[0:train_threshold])
    #sl_train 话题长度
    sl_train_path = os.path.join(save_path,'train_src_len.npy')
    np.save(sl_train_path,topic_lens[0:train_threshold])
    #s_lbl_train 话题分类器
    s_lbl_train = os.path.join(save_path,'train_src_lbl_oh.npy')
    np.save(s_lbl_train,topic_identifiers[0:train_threshold])
    #ti_train 生成文本
    ti_train = os.path.join(save_path,'train_tgt.npy')
    np.save(ti_train,comment_examples[0:train_threshold])
    #tl_train 生成文本长度
    tl_train = os.path.join(save_path,'train_tgt_len.npy')
    np.save(tl_train,comment_lens[0:train_threshold])
    #memory 外部知识
    train_mem_idx = os.path.join(save_path,'train_mem_idx.npy')
    np.save(train_mem_idx,mem[0:train_threshold])

    #测试数据
    #si_test 话题
    si_test_path = os.path.join(save_path,'test_src.npy')
    np.save(si_test_path,topic_examples[train_threshold:test_threshold])
    #sl_test 话题长度
    sl_test_path = os.path.join(save_path,'test_src_len.npy')
    np.save(sl_test_path,topic_lens[train_threshold:test_threshold])
    #s_lbl_test 话题分类器
    s_lbl_test = os.path.join(save_path,'test_src_lbl_oh.npy')
    np.save(s_lbl_train,topic_identifiers[train_threshold:test_threshold])
    #ti_test 生成文本
    ti_test_path = os.path.join(save_path,'test_tgt.npy')
    np.save(ti_test_path,comment_examples[train_threshold,test_threshold])
    #tl_test 生成文本长度
    tl_test_path = os.path.join(save_path,'test_tgt_len.npy')
    np.save(tl_test_path,comment_lens[train_threshold,test_threshold])
    #memory 外部知识
    test_mem_idx_path = os.path.join(save_path,'test_mem_idx.npy')
    np.save(test_mem_idx_path,mem[train_threshold:test_threshold])

    # 评估数据
    # si_ 话题
    si_val_path = os.path.join(save_path, 'val_src.npy')
    np.save(si_val_path, topic_examples[test_threshold:-1])
    # sl_val 话题长度
    sl_val_path = os.path.join(save_path, 'val_src_len.npy')
    np.save(sl_val_path, topic_lens[test_threshold:-1])
    # s_lbl_val 话题分类器
    s_lbl_val = os.path.join(save_path, 'val_src_lbl_oh.npy')
    np.save(s_lbl_train, topic_identifiers[test_threshold:-1])
    # ti_val 生成文本
    ti_val_path = os.path.join(save_path, 'val_tgt.npy')
    np.save(ti_val_path, comment_examples[test_threshold, -1])
    # tl_val 生成文本长度
    tl_val_path = os.path.join(save_path, 'val_tgt_len.npy')
    np.save(tl_val_path, comment_lens[test_threshold, -1])
    # memory 外部知识
    val_mem_idx_path = os.path.join(save_path, 'val_mem_idx.npy')
    np.save(val_mem_idx_path, mem[test_threshold:-1])
    
def load_topic_list(file_path):
    topic_list = []
    with open(file_path, "r") as f:  # 打开文件
        topic_list = f.read().split(' ')  # 读取文件

    return topic_list 

def load_vocab_dict():
    vocab_dict = dict()
    index = 0
    for key in model.wv.vocab.keys() :
        vocab_dict[key] = index
        index+=1


if __name__ == '__main__':
        
    # vocab_dict = dict()
    # vocab_dict['<pad>'] = len(vocab_dict)
    # wv['<pad>']= np.zeros(shape=200.)

    root_path = '/home/shengyu/yeli/textGenerate/dataset'
    origin_file = os.path.join(root_path,'movie_storyline_comment_topic_new.csv')
    topic_list_path = os.path.join(root_path,'topic.txt')
    topic_list = load_topic_list(topic_list_path)
    vocab_dict = np.load(os.path.join(root_path,'vocab_dict.npy')).item()

    handle(origin_file,vocab_dict,topic_list,root_path)
    pass
