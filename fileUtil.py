#coding=utf-8
__author__ = 'Administrator'

def read_dict():
    word_r = []
    word_n = []
    fileHandler = open('word_r0.001.txt', 'r')
    fileHandler.seek(0)
    lines = fileHandler.readlines()
    fileHandler.close()
    for line in lines:
        line = line.split()
        word_r.append(line[0])
        pass
    fileHandler = open('word_n0.05.txt', 'r')
    fileHandler.seek(0)
    lines = fileHandler.readlines()
    fileHandler.close()
    for line in lines:
        line = line.split()
        word_n.append(line[0])
        pass
    return word_r, word_n

def save_r_pre_r(r_pre_r):
    f = open('r_pre_r.txt', 'w')
    for i in range(len(r_pre_r)):
        f.write(' '.join(r_pre_r[i]))
    f.close()

def read_allpat_index():
    f = open('pat_index/pat1_2_3_4.txt', 'r')
    index = []
    for line in f:
        index.append(line.strip())
    return index