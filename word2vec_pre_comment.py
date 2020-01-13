#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 21:23:19 2020

@author: mac
评论放在txt中
"""
import csv
import jieba
import re
import os

def main():
    # windows
    #root_dir = r'A:\研三\textGenerate'
    # linux
    root_dir = '/home/shengyu/yeli/textGenerate'

    dataset_path = os.path.join(root_dir,'dataset')
    filename = os.path.join(os.path.join(dataset_path,'moviedata'),'comments.csv')
    outputfilepath = os.path.join(dataset_path,'comments')

    file_userdict = os.path.join(root_dir,'mystopswords.txt')  # 此处文件名为用户自定义的文件名，内容为不想被分开的词
    jieba.load_userdict(file_userdict)

    #停用词典
    stopwords_path = os.path.join(root_dir,'stopwords.txt')

    #这种公用的变量可以放在循环的外面，只创建一次
    # 创建一个停用词列表
    stopwords = stopwordslist(stopwords_path)
    d = {}

    with open(filename, 'r',encoding='utf8') as f:
        reader = csv.reader(f)
        print(type(reader))
        for row in reader:
            if d.__contains__(row[2]):  # 如果包含这个建，在该建后面追加
                d[row[2]] = d[row[2]] + '。' + row[3]
            else:
                d[row[2]] = row[3]

    d_list = list(d.keys())

    print(d)
    lastID = ''
    file_name = ''
    for item in d_list:  # 遍历
        if item != lastID:  # 新的电影就新建文件
            file_name = os.path.join(outputfilepath,'c_'+ item + '.txt')   # 新建文件
            lastID = item

        sentences = sentence_splitter(d[item])
        with open(file_name, 'a+', encoding='utf8') as f1:
            for sentence in sentences:
                line = re.sub('[a-zA-Z]', '', sentence)
                seg_list = seg_depart(line)
                # seg_list = jieba.cut(sentence,cut_all=False,HMM=True)#对每一句进行分词

                out_list = ' '.join(seg_list.split())
                out_list = out_list + '\n'
                print(out_list)
                if len(out_list) > 4:
                    f1.writelines(out_list)
                    f1.flush()

        #如果文件为空就删除
        if(os.path.getsize(file_name)==0):
            os.remove(file_name)

def sentence_splitter(sentence):
    # 输入一个段落，分成句子，可使用split函数来实现
    sentences = re.split('(。|！|\!|\.|？|\?)',sentence)         # 保留分割符    
    new_sents = []
    for i in range(int(len(sentences)/2)):
        sent = sentences[2*i] + sentences[2*i+1]
        new_sents.append(sent)
    return new_sents

        
def stopwordslist(stopwords_path):
    stopwords = [line.strip() for line in open(stopwords_path,encoding='UTF-8').readlines()]
    return stopwords

def seg_depart(sentence,stopwords):
    # 对文档中的每一行进行中文分词
    print("正在分词")
    sentence_depart = jieba.cut(sentence.strip())

   
    # 输出结果为outstr
    outstr = ''
    # 去停用词
    for word in sentence_depart:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr



if __name__=='__main__':
    main()
    print('end')

           
            
            
        
            
            
        