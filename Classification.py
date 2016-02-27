# -*- coding: utf-8 -*-
import os
import sys
from vector import vector_create
from sklearn import svm
reload(sys)  
sys.setdefaultencoding('utf8') 


def modle(train_array,flag):
    print "svm start"
    #rbf svm
    #clf = svm.SVC(C=10)
    #linear svm
    clf = svm.LinearSVC(dual=False,C=10)
    clf.fit(train_array,flag)
    print "svm finished"
    return clf
    
    pass 
def predict(clf,test):
    return clf.predict(test)
    pass