#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__doc__ = 'description'
__author__ = '13314409603@163.com'
import csv
if __name__ == '__main__':
    string = "      "
    print(string.strip())
    print(len(string.strip()))
    print('end!')

    with open(r'A:\研三\textGenerate\dataset\movies.csv', 'r',encoding='utf8') as f:
        reader = csv.reader(f)
        print(type(reader))
        next(f)
        count = 0
        for row in reader:
            count+=1

        print(count)
        count2 = 0
        # reader.reset()
        for row in reader:
            count2+=1
        print(count2)