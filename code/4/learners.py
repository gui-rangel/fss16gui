import table, rows, syms, nums
import sys

def knn(train, test, k):
    train_table = table.Table()
    train_table.add_rows(train)
    test_table = table.Table()
    test_table.add_rows(test)

    for num,row in enumerate(test_table.rows):
        closest = train_table.closest_row(row)
        print "{}  Actual: {} - Predicted: {}".format(num+1,closest[-1],row[-1])

def knn_kd(train, test, k):
    train_table = table.Table()
    train_table.add_rows(train)
    test_table = table.Table()
    test_table.add_rows(test)

    for num,row in enumerate(test_table.rows):
        closest = train_table.closest_row(row)
        print "{}  Actual: {} - Predicted: {}".format(num+1,closest[-1],row[-1])
    

if __name__ == "__main__":
    knn(sys.argv[1],sys.argv[1],1)