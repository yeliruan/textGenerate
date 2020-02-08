#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 8 16:33:12 2020

@author: ruanyeli
"""

import csv
import os

def count(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        print(type(reader))
        next(f)
        count = 0
        for row in reader:
            count += 1
        return count


if __name__ == '__main__':
    root_path = '/home/shengyu/yeli/textGenerate/dataset'
    origin_path = os.path.join(root_path, 'moviedata')

    movie_data = os.path.join(origin_path, 'movies.csv')
    comment_data = os.path.join(origin_path, 'comments.csv')
    person_data = os.path.join(origin_path, 'person.csv')
    users_data = os.path.join(origin_path, 'users.csv')

    movie_number = count(movie_data)
    comment_number = count(comment_data)
    person_number = count(person_data)
    users_number = count(users_data)

    print('movie_number',movie_number)
    print('comment_number',comment_number)
    print('person_number',person_number)
    print('users_number',users_number)

