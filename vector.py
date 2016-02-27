# -*- coding: utf-8 -*-
import jieba
import jieba.analyse
import os
import numpy as np
import sys
reload(sys)  
sys.setdefaultencoding('utf8') 
def vector_create(string_v, word_r, word_n):
    # string cut word and save as Array
    c1 = string_v.count('!')
    c2 = string_v.count('！')
    wordArray = " ".join(jieba.cut(string_v, cut_all=True))
    wordArray = wordArray.split()
    # the length of vector
    length = word_r.__len__()+word_n.__len__()
    vector = [0 for x in xrange(0, length+2)]
    #concider lenght of the  text
    vector[length] = len(string_v)
    vector[length+1] = c1 + c2
    for word in wordArray:
        for i in xrange(0, word_r.__len__()-1):
            if word == word_r[i]:
                vector[i] += 1
                pass
            pass
        for j in xrange(0, word_n.__len__()-1):
            if word == word_n[j]:
                vector[word_r.__len__()-1+j] += 1
                pass
            pass
    return vector

def bayes_vector_create(string_v, word_r, word_n):
    length = word_r.__len__()+word_n.__len__()
    vector = [0 for x in xrange(0, length)]
    for word in string_v.split(','):
        for i in xrange(0, word_r.__len__()):
            if word == word_r[i]:
                vector[i] += 1
        for j in xrange(0, word_n.__len__()):
            if word == word_n[j]:
                vector[word_r.__len__()+j] += 1
    return vector

def create_vector(content, word_vector):
    vector = [0 for x in xrange(0, len(word_vector))]
    words = jieba.cut(content, cut_all=True)
    for word in words:
        for i in xrange(0, len(word_vector)):
            if word == word_vector[i]:
                vector[i] += 1
    return vector





