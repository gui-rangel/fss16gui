from table import Table
import random
import numpy as np
import math
from ABCD import ABCD

def data_generator(table):
    data = table.rows
    while len(data) < 2000:
        data.append(table.rows[random.randint(0, len(table.rows) - 1)])
    ri1=ri2=rd1=rd2= []
    ri1,rd1,ri2,rd2 = randomizer(data, ri1, rd1, ri2, rd2)
    random.shuffle(rd1)
    random.shuffle(rd2)
    print rd1[0]
    newData = rd1 + rd2
    return newData

def randomizer(data, ri1, rd1, ri2, rd2):
    class_labels = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

    label = class_labels[0]
    while len(ri1) < 500:
        randIndex = random.randint(0, len(data) - 1)
        randomRow = data[randIndex]
        if ((randomRow[-1] == label) & (randIndex not in ri1)):
            ri1.append(randIndex)
            rd1.append(randomRow)

    label = class_labels[1]
    while len(ri1) < 1000:
        randIndex = random.randint(0, len(data) - 1)
        randomRow = data[randIndex]
        if ((randomRow[-1] == label) & (randIndex not in ri1)):
            ri1.append(randIndex)
            rd1.append(randomRow)

    label = class_labels[0]
    while len(ri2) < 100:
        randIndex = random.randint(0, len(data) - 1)
        randomRow = data[randIndex]
        if ((randomRow[-1] == label) & (randIndex not in ri2)):
            ri2.append(randIndex)
            rd2.append(randomRow)

    label = class_labels[1]
    while len(ri2) < 400:
        randIndex = random.randint(0, len(data) - 1)
        randomRow = data[randIndex]
        if ((randomRow[-1] == label) & (randIndex not in ri2)):
            ri2.append(randIndex)
            rd2.append(randomRow)

    label = class_labels[2]
    while len(ri2) < 1000:
        randIndex = random.randint(0, len(data) - 1)
        randomRow = data[randIndex]
        if ((randomRow[-1] == label) & (randIndex not in ri2)):
            ri2.append(randIndex)
            rd2.append(randomRow)

    return ri1,rd1,ri2,rd2

def nb(data):
    for i in xrange(0, 5):
        if i==0:
            endIndexTrainData = 100
            startIndex = 0
            endIndexTestData = 100
        else:
            endIndexTrainData = (i)*100
            endIndexTestData = (i+1)*100
            startIndex = endIndexTrainData + 1
        train = data[0:endIndexTrainData]
        test = data[startIndex:endIndexTestData]
        train_label = test_label = data_train = data_test = []
        labelMap = {'Iris-setosa': -1,'Iris-versicolor': 0,'Iris-virginica': 1}
        for x in train:
            train_label.append(labelMap[x[-1]])
            data_train.append(x[:-1])
        for x in test:
            test_label.append(labelMap[x[-1]])
            data_test.append(x[:-1])
        from sklearn.naive_bayes import GaussianNB
        NB = GaussianNB()
        predict = NB.fit(np.array(data_train),train_label).predict(data_test)
        abcd = ABCD(before=test_label, after=predict)
        pd = np.array([j.stats()[0] for j in abcd()])
        c1 = pd[0]
        c2 = pd[1]
        try: c3 = pd[2]
        except: c3 = 0
        print "Era: " + str(i+1)
        print "Class 1: " + str(c1)
        print "Class 2: " + str(c2)
        print "Class 3: " + str(c3)
        l1 = l2 = []
        score = oldScore = 0
        if i == 0:
            l1 = [c1, c2, c3]
            l2 = l1
        else:
            l1 = l2
            l2 = [c1, c2, c3]
            oldScore = score
            score = a12(l1, l2)
        print "a12 Score: " + str(score)
        if math.fabs(oldScore - score) > 0.2 * oldScore:
            print "Anamoly was detected."
        print ""

def a12(self, list1, list2):
    more = same = 0.0
    for x in sorted(list1):
        for y in sorted(list2):
            if x == y:
                same += 1
            elif x > y:
                more += 1
    return (more + 0.5*same) / (len(list1)*len(list2))

if __name__ == "__main__":
    table = Table("data.csv")
    data = data_generator(table)
    nb(data)
