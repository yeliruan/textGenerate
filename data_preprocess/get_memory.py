#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 15:27:05 2020

@author: mac
"""
import csv
import string


def str_count2(str):
    '''找出字符串中的中英文、空格、数字、标点符号个数'''
    count_en = count_dg = count_sp = count_zh = count_pu = 0

    for s in str:
        # 英文
        if s in string.ascii_letters:
            count_en += 1
        # 数字
        elif s.isdigit():
            count_dg += 1
        # 空格
        elif s.isspace():
            count_sp += 1
        # 中文
        elif s.isalpha():
            count_zh += 1
        # 特殊字符
        else:
            count_pu += 1

    return count_en+count_dg+count_sp+count_zh+count_pu


# def str_count2(str):
#     count_ = 0
#     for s in str:
#         # 中文字符范围
#         if '\u4e00' <= s <= '\u9fff':
#             count_ = count_ + 1
#
#     return count_


if __name__ == '__main__':

    origin_file = '/Users/mac/Desktop/movie_storyline_comment_topic_fuwu.csv'

    with open(origin_file, 'r') as f:

        reader = csv.reader(f)
        count = 0
        word_count = 0
        next(f)
        for row in reader:
            count = count + 1
            word_count = word_count + str_count2(row[0])
            word_count = word_count + str_count2(row[1])
            word_count = word_count + str_count2(row[2])
            word_count = word_count + str_count2(row[3])
            word_count = word_count + str_count2(row[4])

        print(count)
        print(word_count)


