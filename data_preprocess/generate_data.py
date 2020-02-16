#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__doc__ = 'description' \
          '将movie_storyline_comment_topic.csv初始样例转换为CTEG输入数据格式'
__author__ = '13314409603@163.com'

import csv
import numpy as np
from util.constant import PAD_TAG,UNKNOW_TAG,BEGIN_TAG,END_TAG
from util.constant import TRAIN_TEST_VAL
import os
import sys

def handle(origin_file,vocab_dict,topic_list,save_path,backgroud_knowledge_max_length=187):

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

    total_examples_length = 0
    count = 0


    with open(origin_file, 'r',encoding='utf8') as f:
        reader = csv.reader(f)
        #去掉第一行header
        next(f)

        for row in reader:
            count += 1
            movie_id = row[0]
            comment_str = row[1]
            rating_str = row[2]
            storyline_str = row[3]
            topic_str = row[4]
            
            topics = topic_str.split(' ')
        
            topic_examples_temp = []
            
            for topic in topics:
                if topic != '':
                    try:
                        topic_examples_temp.append(vocab_dict[topic])
                    except KeyError:
                        topic_examples_temp.append(vocab_dict[UNKNOW_TAG])
                else:
                    print('存在空字符:'+topic_str)
            topic_examples.append(topic_examples_temp)

            topic_lens.append(len(topics))

            topic_identifier = [1 if topic in topics else 0 for topic in topic_list]
            topic_identifier.append(0)
            topic_identifiers.append(topic_identifier)

            comment_words = comment_str.split(' ')
            comment_examples_temp = []
            for word in comment_words:
                if word != '':
                    try:
                        comment_examples_temp.append(vocab_dict[word])
                    except KeyError:
                        comment_examples_temp.append(vocab_dict[UNKNOW_TAG])
                else:
                    print('存在空字符:'+comment_str)
            comment_examples.append(comment_examples_temp)

            comment_lens.append(len(comment_words))

            storyline_words = storyline_str.split(' ')
            #将简介填充或截取
            if(len(storyline_words)>backgroud_knowledge_max_length):
                storyline_words = storyline_words[0:backgroud_knowledge_max_length]
            else:
                storyline_words.extend([PAD_TAG for i in range(backgroud_knowledge_max_length-len(storyline_words))])
            assert len(storyline_words)==backgroud_knowledge_max_length


            # #简介word转id
            mem_temp = []
            for word in storyline_words:
                if word != '':
                    try:
                        mem_temp.append(vocab_dict[word])
                    except KeyError:
                        mem_temp.append(vocab_dict[UNKNOW_TAG])
                else:
                    print('存在空字符:'+storyline_str)
            mem.append(mem_temp)

    print('样例总数：'+str(count))
    total_examples_length = count
    #训练：测试：评估分段

    train_threshold = int(TRAIN_TEST_VAL[0]*total_examples_length)
    test_threshold = int(TRAIN_TEST_VAL[1]*total_examples_length+train_threshold)
    print('%s size is %d' % (type(topic_identifiers),sys.getsizeof(topic_identifiers)))
    #训练数据
    # si_train 话题
    si_train_path = os.path.join(save_path,'train_src.npy')
    np.save(si_train_path,topic_examples[0:train_threshold])
    # sl_train 话题长度
    sl_train_path = os.path.join(save_path,'train_src_len.npy')
    np.save(sl_train_path,topic_lens[0:train_threshold])
    # s_lbl_train 话题分类器
    s_lbl_train = os.path.join(save_path,'train_src_lbl_oh.npy')
    np.save(s_lbl_train,topic_identifiers[0:train_threshold])
    # ti_train 生成文本
    ti_train = os.path.join(save_path,'train_tgt.npy')
    np.save(ti_train,comment_examples[0:train_threshold])
    # tl_train 生成文本长度
    tl_train = os.path.join(save_path,'train_tgt_len.npy')
    np.save(tl_train,comment_lens[0:train_threshold])
    #memory 外部知识
    train_mem_idx = os.path.join(save_path,'train_mem_idx_120_concept.npy')
    np.save(train_mem_idx,mem[0:train_threshold])

    #测试数据
    # si_test 话题
    si_test_path = os.path.join(save_path,'tst.src.npy')
    np.save(si_test_path,topic_examples[train_threshold:test_threshold])
    # sl_test 话题长度
    sl_test_path = os.path.join(save_path,'tst.src.len.npy')
    np.save(sl_test_path,topic_lens[train_threshold:test_threshold])
    # s_lbl_test 话题分类器
    s_lbl_test = os.path.join(save_path,'tst.src.lbl.oh.npy')
    np.save(s_lbl_test,topic_identifiers[train_threshold:test_threshold])
    # ti_test 生成文本
    ti_test_path = os.path.join(save_path,'tst.tgt.npy')
    np.save(ti_test_path,comment_examples[train_threshold:test_threshold])
    # tl_test 生成文本长度
    tl_test_path = os.path.join(save_path,'tst.tgt.len.npy')
    np.save(tl_test_path,comment_lens[train_threshold:test_threshold])
    #memory 外部知识
    test_mem_idx_path = os.path.join(save_path,'tst.mem.idx.120.concept.npy')
    np.save(test_mem_idx_path,mem[train_threshold:test_threshold])

    # 评估数据
    # si_ 话题
    si_val_path = os.path.join(save_path, 'val.src.npy')
    np.save(si_val_path, topic_examples[test_threshold:-1])
    # sl_val 话题长度
    sl_val_path = os.path.join(save_path, 'val.src.len.npy')
    np.save(sl_val_path, topic_lens[test_threshold:-1])
    # s_lbl_val 话题分类器
    s_lbl_val = os.path.join(save_path, 'val.src.lbl.oh.npy')
    np.save(s_lbl_val, topic_identifiers[test_threshold:-1])
    # ti_val 生成文本
    ti_val_path = os.path.join(save_path, 'val.tgt.npy')
    np.save(ti_val_path, comment_examples[test_threshold:-1])
    # tl_val 生成文本长度
    tl_val_path = os.path.join(save_path, 'val.tgt.len.npy')
    np.save(tl_val_path, comment_lens[test_threshold: -1])
    # memory 外部知识
    val_mem_idx_path = os.path.join(save_path, 'val.mem.idx.120.concept.npy')
    np.save(val_mem_idx_path, mem[test_threshold:-1])
    
def load_topic_list(file_path):
    with open(file_path, 'r',encoding='utf8') as f:  # 打开文件
        topic_list = f.read().split(' ')  # 读取文件
    return topic_list 

def stopwordslist(stopword_file):
    stopwords = [line.strip() for line in open(stopword_file,encoding='UTF-8').readlines()]
    return stopwords

if __name__ == '__main__':

    # root_path = '/home/shengyu/yeli/textGenerate/dataset'
    root_path = r'A:\研三\textGenerate\dataset'

    origin_file = os.path.join(root_path,'movie_storyline_comment_similarity_topic_new.csv')
    # origin_file = os.path.join(root_path,'topic_small.csv')
    topic_list_path = os.path.join(root_path,'topic_new.txt')
    topic_list = load_topic_list(topic_list_path)
    np_load_old = np.load
    np.load = lambda *a, **k: np_load_old(*a, allow_pickle=True, **k)
    vocab_dict = np.load(os.path.join(root_path,'vocab_dict.npy')).item()

    save_path = os.path.join(root_path,'cteg')
    handle(origin_file,vocab_dict,topic_list,save_path)
    print('end')
