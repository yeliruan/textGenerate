#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 5 11:12:57 2020

@author: mac
"""
import numpy as np
import os
import pickle

if __name__=='__main__':

    root_path = '/home/shengyu/yeli/textGenerate/dataset/cteg'
    train_si = np.load(os.path.join(root_path, 'train_src.npy'))
    train_tgt = np.load(os.path.join(root_path, 'train_tgt.npy'))

    test_src = np.load(os.path.join(root_path, 'tst.src.npy'))
    test_tgt = np.load(os.path.join(root_path, 'tst.tgt.npy'))
    val_src = np.load(os.path.join(root_path, 'val.src.npy'))
    val_tgt =  np.load(os.path.join(root_path, 'val.tgt.npy'))

    print(len(train_si))
    print(len(train_tgt))

    print(len(test_src))
    print(len(test_tgt))

    print(len(val_src))
    print(len(val_tgt))
