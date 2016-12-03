from table import Table
from random import random,shuffle,seed
import time
import numpy as np
import pandas
from sk import rdivDemo
from ABCD import ABCD


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

def knn(table, data_train, data_test):
    prediction=[]
    for a,row in enumerate(data_test):
        closestRow,i = table.minDistance(row, data_train)
        actual, predicted = row[-1], closestRow[-1]
        prediction.append(predicted)
    return prediction

def kmeans(data_train, data_test):
    from sklearn.cluster import MiniBatchKMeans
    kmeans = MiniBatchKMeans(init='random',n_clusters=20, n_init=20,batch_size=20,compute_labels=True)
    kmeans.fit(data_train)
    k_means_cluster_centers = np.sort(kmeans.cluster_centers_, axis=0)

    from sklearn.metrics.pairwise import pairwise_distances_argmin
    k_means_labels = pairwise_distances_argmin(data_train, k_means_cluster_centers)
    predict=kmeans.predict(data_test)
    prediction=[]
    for y in predict:
        prediction.append(data_train[y][-1])
    return prediction

def kdtree(data_train, data_test):
    from sklearn.neighbors import KDTree
    tree = KDTree(data_train, leaf_size=2, metric='euclidean')
    _, ind=tree.query(data_test,k=1)

    predict=[item for sublist in ind for item in sublist]
    prediction=[]
    for y in predict:
        prediction.append(data_train[y][-1])
    return prediction
        

if __name__ == '__main__':
    datasets=['diabetes.csv','jedit-3.2.csv','ivy-2.0.csv']
    folds=5
    seed(1)
    pd, pf, rt = {},{},{} 
    trees=['knn','kmeans','kd']
    for k in datasets:
        pd[k], pf[k], rt[k] = {},{},{}
        for x in trees: pd[k][x], pf[k][x], rt[k][x] =[], [], 0
        table = Table('./'+k)
        for i in xrange(folds):
            shuffle(table.rows)
            for index in xrange(folds):
                data_train, data_test = split(table.rows, folds=folds, index=index)
                train_label, test_label = [], []
                for x in data_train: train_label.append(x[-1])
                for x in data_test: test_label.append(x[-1])

                start_time = time.time()
                prediction = knn(table, data_train, data_test)
                abcd = ABCD(before=test_label, after=prediction)
                pd[k]['knn'].append(np.array([j.stats()[0] for j in abcd()])[0])
                pf[k]['knn'].append(([j.stats()[1] for j in abcd()])[0])
                rt[k]['knn'] += time.time() - start_time

                start_time = time.time()
                prediction = kmeans(data_train, data_test)
                abcd = ABCD(before=test_label, after=prediction)
                pd[k]['kmeans'].append(np.array([j.stats()[0] for j in abcd()])[0])
                pf[k]['kmeans'].append(([j.stats()[1] for j in abcd()])[0])
                rt[k]['kmeans'] += time.time() - start_time

                start_time = time.time()
                prediction = kdtree(data_train, data_test)
                abcd = ABCD(before=test_label, after=prediction)
                pd[k]['kd'].append(np.array([j.stats()[0] for j in abcd()])[0])
                pf[k]['kd'].append(([j.stats()[1] for j in abcd()])[0])
                rt[k]['kd'] += time.time() - start_time

    for feature in datasets:
        tmp = []
        temp1=[]
        print(feature)
        for tree in trees:
                tmp.append([tree] + pd[feature][tree])
                temp1.append([tree] + pf[feature][tree])
        print("Recall")
        print(rdivDemo(tmp))
        print("False Alarm")
        print(rdivDemo(temp1))
        print("\n")

    print(rt)
