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

    with open(r'A:\研三\textGenerate\dataset\test.csv', 'a',newline='',encoding='utf8') as f:
        writer = csv.writer(f)
        writer.writerow(['bob',23])
        writer.writerow(['marry',26])