from table import Table
from random import random,shuffle,seed
import time
import numpy as np
import pandas
from sk import rdivDemo
from ABCD import ABCD
import num


def split(corpus, folds=5, index=0):
    i_major, i_minor = [], []
    l = len(corpus)
    corpus=pandas.DataFrame({"A":corpus})
    for i in range(0, folds):
        if i == index:
            i_minor.extend(range(int(i * l / folds), int((i + 1) * l / folds)))
        else:
            i_major.extend(range(int(i * l / folds), int((i + 1) * l / folds)))
    return list(corpus.iloc[i_major,].values.flatten()), list(corpus.iloc[i_minor,].values.flatten())

def nb(data_train, data_test, train_label):
    from sklearn.naive_bayes import GaussianNB
    nb = GaussianNB()
    nb.fit(data_train,train_label)
    prediction = nb.predict(data_test)
    return prediction

if __name__ == '__main__':
    datasets=['diabetes.csv','jedit-3.2.csv','ivy-2.0.csv', 'arc.csv', 'camel-1.0.csv']
    folds=5
    seed(1)
    pd, pf, rt = {},{},{} 
    learners =['nb', 'width', 'frequency']
    for k in datasets:
        pd[k], pf[k], rt[k] = {},{},{}
        for x in learners: pd[k][x], pf[k][x], rt[k][x] =[], [], 0
        table = Table('./'+k)
        for i in xrange(folds):
            shuffle(table.rows)
            for index in xrange(folds):
                oldTable = table

                data_train, data_test = split(table.rows, folds=folds, index=index)
                train_label, test_label = [], []
                for x in data_train: train_label.append(x[-1])
                for x in data_test: test_label.append(x[-1])
                
                start_time = time.time()
                prediction = nb(data_train, data_test, train_label)
                abcd = ABCD(before=test_label, after=prediction)
                pd[k]['nb'].append(np.array([j.stats()[0] for j in abcd()])[0])
                pf[k]['nb'].append(([j.stats()[1] for j in abcd()])[0])
                rt[k]['nb'] += time.time() - start_time

                for col in table.cols:
                    if (isinstance(col,num.Num)):
                        col.discretize("width", 10)
                data_train, data_test = split(table.rows, folds=folds, index=index)
                train_label, test_label = [], []
                for x in data_train: train_label.append(x[-1])
                for x in data_test: test_label.append(x[-1])
                
                start_time = time.time()
                prediction = nb(data_train, data_test, train_label)
                abcd = ABCD(before=test_label, after=prediction)
                pd[k]['width'].append(np.array([j.stats()[0] for j in abcd()])[0])
                pf[k]['width'].append(([j.stats()[1] for j in abcd()])[0])
                rt[k]['width'] += time.time() - start_time
                
                table = oldTable
                for col in table.cols:
                    if (isinstance(col,num.Num)):
                        col.discretize("frequency", 10)
                data_train, data_test = split(table.rows, folds=folds, index=index)
                train_label, test_label = [], []
                for x in data_train: train_label.append(x[-1])
                for x in data_test: test_label.append(x[-1])
                
                start_time = time.time()
                prediction = nb(data_train, data_test, train_label)
                abcd = ABCD(before=test_label, after=prediction)
                pd[k]['frequency'].append(np.array([j.stats()[0] for j in abcd()])[0])
                pf[k]['frequency'].append(([j.stats()[1] for j in abcd()])[0])
                rt[k]['frequency'] += time.time() - start_time


    for feature in datasets:
        tmp = []
        temp1=[]
        print(feature)
        for learner in learners:
                tmp.append([learner] + pd[feature][learner])
                temp1.append([learner] + pf[feature][learner])
        print("pd")
        print(rdivDemo(tmp))
        print("pf")
        print(rdivDemo(temp1))
        print("\n")

    # print(rt)
