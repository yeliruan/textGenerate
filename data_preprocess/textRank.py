#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 21:38:10 2019

@author: mac
"""

# -*- encoding:utf-8 -*-
from textrank4zh import TextRank4Keyword, TextRank4Sentence
import codecs

file = r"/Users/mac/Desktop/test1.txt"
text = codecs.open(file, 'r', 'utf-8').read()

word = TextRank4Keyword()

word.analyze(text, window=2, lower=True)
w_list = word.get_keywords(num=10, word_min_len=1)

print('关键词:')
print
for w in w_list:
    print(w.word, w.weight)


print
phrase = word.get_keyphrases(keywords_num=5, min_occur_num=1)

print('关键词组:')
print
for p in phrase:
    print(p)
print
sentence = TextRank4Sentence()

sentence.analyze(text, lower=True)
s_list = sentence.get_key_sentences(num=3, sentence_min_len=5)

print('关键句:')
print
for s in s_list:
    print(s.sentence, s.weight)
print