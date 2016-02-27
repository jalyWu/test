# -*- coding: utf-8 -*-
import sys

from vector import vector_create
from Classification import modle
from Classification import predict
import fileUtil


reload(sys)  
sys.setdefaultencoding('utf8') 

if __name__ == '__main__':
    print "reading"
    fileHandler = open ('data\\data.txt')
    fileHandler.seek(0)
    lines = fileHandler.readlines()
    fileHandler.close()
    list_train=[]
    list_test=[]
    # choose the train and test set
    # count=0
    # is_rubbish=0
    print 'divide data'
    for line in lines:
        line = line.split("\t", 2)
    #     result = filter_pat3_t(line[2])
    #     if result:
    #         count+=1
    #         if line[1]=='1':
    #             is_rubbish+=1
    # print count
    # print 'radio:', float(is_rubbish)/count
        if(int(line[0])%5 == 0):
            list_test.append(line)
        else:
            list_train.append(line)
        pass
    train_array=[]
    test_array=[]
    flag = []
    answer = []
    result = []
    word_r, word_n = fileUtil.read_dict()
    print 'set train vector'
    for list1 in list_train:
        train_array.append(vector_create(list1[2], word_r, word_n))
        flag.append(list1[1])
        pass
    print 'set test vector'
    for list2 in list_test:
        test_array.append(vector_create(list2[2], word_r, word_n))
        answer.append(list2[1])
        pass
    print "read finished"
    # svm
    clf = modle(train_array, flag)
    result = predict(clf, test_array)
    sum_rubbish = 0
    sum_normal = 0
    pre_rubbish = 0
    pre_normal = 0
    right_rubbish = 0
    right_normal = 0
    r_pre_n = []
    for x in xrange(0, len(result)-1):
        if result[x] == answer[x]:
            if result[x] == "1":
                sum_rubbish += 1
                pre_rubbish += 1
                right_rubbish += 1
            else:
                sum_normal += 1
                pre_normal += 1
                right_normal += 1
                pass
            pass
        else:
            if result[x] == "1":
                pre_rubbish += 1
                sum_normal += 1
            else:
                pre_normal += 1
                sum_rubbish += 1
                r_pre_n.append(list_test[x])
                pass
    # save_r_pre_n(r_pre_n)
    accuracy_rubbish = 0.
    recall_rubbish = 0.
    accuracy_normal = 0.
    recall_normal = 0.
    F = 0.
    accuracy_rubbish = float(right_rubbish)/pre_rubbish
    recall_rubbish = float(right_rubbish)/sum_rubbish
    accuracy_normal = float(right_normal)/pre_normal
    recall_normal = float(right_normal)/sum_normal
    F = 0.7*(0.65*accuracy_rubbish+0.35*recall_rubbish)+0.3*(0.65*accuracy_normal+0.35*recall_normal)
    print "right_rubbish:%d" %right_rubbish
    print "sum_rubbish:%d" %sum_rubbish
    print "accuracy_rubbish:%s" %accuracy_rubbish
    print "recall_rubbish:%s" %recall_rubbish
    print "accuracy_normal:%s"%accuracy_normal
    print "recall_normal:%s"%recall_normal
    print "F:%s" %F