# -*- coding: utf-8 -*-
import sys

from sklearn import svm
from sklearn.externals import joblib

from vector import vector_create
from pre_process.boge import fileUtil

reload(sys)  
sys.setdefaultencoding('utf8') 

if __name__ == '__main__':
    word_r, word_n = fileUtil.read_dict()
    print "reading"
    fileHandler_t = open('data\\test.txt')
    fileHandler_t.seek(0)
    lines_t = fileHandler_t.readlines()
    fileHandler_t.close()
    fileHandler_tr = open('data\\data.txt')
    fileHandler_tr.seek(0)
    lines_tr = fileHandler_tr.readlines()
    fileHandler_tr.close()
    print "read finished"

    vector_array = []
    train_array = []
    flag = []
    for line in lines_t:
        line = line.split('\t',1)
        # cut word  thrid arrary of sentence should change to 1 in test set
        vector_array.append(vector_create(line[1], word_r, word_n))
        pass
    for line in lines_tr:
        line = line.split('\t', 2)
        train_array.append(vector_create(line[2], word_r, word_n))
        flag.append(line[1])
        pass
    print "svm start"
    # clf = svm.SVC()
    clf = svm.LinearSVC(dual=False, C=10)
    clf.fit(train_array, flag)
    joblib.dump(clf, 'classifiter/svc_classifiter.pkl')
    # clf = joblib.load('classifiter.pkl')
    print "svm finished"
    print "predicting"
    fileHandler_out = open('dest_result/svc_result_14.csv', "w")
    num = 800001
    result = []
    for pr in vector_array:
        tag = []
        tag.append(str(num))
        tag.append(clf.predict(pr))
        result.append(tag)
        num += 1
        pass
    for r in result:
        fileHandler_out.write(r[0])
        fileHandler_out.write(',')
        fileHandler_out.write(r[1])
        fileHandler_out.write('\n')
    fileHandler_out.close()
