#coding=utf-8
__author__ = 'Administrator'

import re

def filter_pat1(content):
    l = len(content[2])
    pat = re.compile('x+')
    mat = pat.search(content[2])
    if mat:
        result = re.subn('x+', '', content[2])[0]
        if float(len(result))/l < 0.5:
            print str(content)
            return True

def filter_pat1_t(content):
    l = len(content)
    pat = re.compile('x+')
    mat = pat.search(content)
    if mat:
        result = re.subn('x+', '', content)[0]
        if float(len(result))/l < 0.5:
            print content
            return True

def filter_pat2(content):
    dic = ['鼠', '牛', '虎', '兔', '龙', '蛇', '马', '羊', '猴', '鸡', '狗', '猪']
    flag = [x for x in dic if x in content[2]]
    if len(flag) == 0:
        flag = False
    else:
        flag = True
    pat = re.compile('x+期')
    mat = pat.search(content[2])
    if mat and flag:
        print ' '.join(content)
        return True

def filter_pat2_t(content):
    dic = ['鼠', '牛', '虎', '兔', '龙', '蛇', '马', '羊', '猴', '鸡', '狗', '猪']
    flag = [x for x in dic if x in content]
    if len(flag) == 0:
        flag = False
    else:
        flag = True
    pat = re.compile('x+期')
    mat = pat.search(content)
    if mat and flag:
        print ''.join(content)
        return True

def filter_pat2_dif2_t(content):
    dic = ['鼠', '牛', '虎', '兔', '龙', '蛇', '马', '羊', '猴', '鸡', '狗', '猪']
    flag = set([x for x in dic if x in content])
    pat = re.compile('x+期')
    mat = pat.search(content)
    if len(flag) > 2 and not mat:
        return True
    else:
        return False

def filter_pat3(content):
    source = content
    if len(content) < 22:
        content = content
    else:
        content = content[0:22]
    if '你好' in content or '您好' in content:
        print ''.join(source)
        return True

def filter_pat3_t(content):
    source = content
    if len(content) < 22:
        content = content
    else:
        content = content[0:22]
    if '你好' in content or '您好' in content:
        print ''.join(source)
        return True

def filter_pat4(f):
    count = 0
    is_rubbish = 0
    pat = re.compile('x+')
    for line in f:
        line = line.split("\t", 2)
        mat = pat.search(line[2])
        flag = '积分' in line[2]
        result = '会员' in line[2]
        if mat and flag and result:
            count += 1
            if line[1] == '1':
                is_rubbish += 1
            else:
                print ' '.join(line)
    print count
    print 'radio:', float(is_rubbish)/count

def filter_pat4_t(f):
    index = []
    pat = re.compile('x+')
    for line in f:
        line = line.split("\t")
        mat = pat.search(line[1])
        flag = '积分' in line[1]
        result = '会员' in line[1]
        if mat and flag and result:
            index.append(line[0])
    return index

def filter_pat6_t(f):
    index0 = []
    index1 = []
    count0 = 0
    count1 = 0
    length0 = 0
    length1 = 0
    pat = re.compile(u'x{3,}[\u4e00-\u9fa5]{0,4}$')
    for line in f:
        line = line.split('\t', 2)
        mat = pat.search(line[2].decode())
        if mat and line[1] == '0':
            # if ',' in line[2] or '。' in line[2] or '!' in line[2]:
            #     print '\t'.join(line)
            count0+=1
            length0+=len(line[2])
            index0.append(line)
        if mat and line[1] == '1':
            if '，' not in line[2] and '。' not in line[2] and '！' not in line[2]:
                print '\t'.join(line)
            count1 += 1
            length1+=len(line[2])
            index1.append(line)
    print '0  ',length0/float(count0)
    print '1  ',length1/float(count1)
    return index0,index1

def filter_pat1_6_t(f):
    index = []
    radio = 0
    pat = re.compile(u'x{5,}[\u4e00-\u9fa5]{1,3}$')
    for line in f:
        line = line.split('\t', 1)
        l = len(line[1])
        mat = pat.search(line[1].decode())
        pat1 = re.compile('x+')
        mat1 = pat1.search(line[1])
        if mat1:
            result = re.subn('x+', '', line[1])[0]
            radio = float(len(result))/l
        if mat and radio > 0.5:
            index.append(line[0])
    return index

def filter_pat7(content):
    pat = re.compile('x{3,}')
    mat = pat.findall(content)
    flag = False
    if '，' not in content and '。'not in content:
        flag = True
    if len(mat) > 2 and flag:
        return True

def get_pat5_t_index(f):
    index = []
    for line in f:
        line = line.split('\t', 1)
        if '!' in line[1] or '！' in line[1]:
            index.append(line[0])
    return index


def get_pat1_t_index(f):
    index = []
    for line in f:
        line = line.split('\t', 1)
        flag = filter_pat1_t(line[1])
        if flag:
            index.append(line[0])
    return index

def get_pat2_t_index(f):
    index = []
    for line in f:
        line = line.split('\t', 1)
        flag = filter_pat2_t(line[1])
        if flag:
            index.append(line[0])
    return index

def get_pat3_t_index(f):
    index = []
    for line in f:
        line = line.split('\t', 1)
        flag = filter_pat3_t(line[1])
        if flag:
            index.append(line[0])
    return index

