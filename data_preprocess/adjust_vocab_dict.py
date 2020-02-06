"""
Created on  Feb 7 11:56:36 2020

@author: mac
"""


import numpy as np


def get_vocab_dict(dict_path, dict_path_new):
    vocab_dict = np.load(dict_path,allow_pickle=True).item()

    vocab_dict['<GO>'] = len(vocab_dict)
    vocab_dict['<UNK>'] = len(vocab_dict)
    vocab_dict['<EOS>'] = len(vocab_dict)

    print(vocab_dict['<PAD>'])
    print(vocab_dict['<GO>'])
    print(vocab_dict['<UNK>'])
    print(vocab_dict['<EOS>'])

    np.save(dict_path_new,vocab_dict)


if __name__=='__main__':
    dict_path = '/home/usr/shengyu/CTEG/data/word_dict_zhihu.npy'
    dict_path_new = '/home/usr/shengyu/CTEG/data/word_dict_zhihu_new.npy'

    # dict_path = '/Users/mac/workspace/textGenerate/data/word_dict_zhihu.npy'
    # dict_path_new = '/Users/mac/workspace/textGenerate/data/word_dict_zhihu_new.npy'
    get_vocab_dict(dict_path,dict_path_new)

