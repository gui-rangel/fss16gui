import table, rows, syms, nums
import sys, random, collections

def knn(train, test, k):
    train_table = table.Table()
    train_table.add_rows(train)
    test_table = table.Table()
    test_table.add_rows(test)

    for num,row in enumerate(test_table.rows):
        closest = train_table.closest_row(row)
        # print "{}  Actual: {} - Predicted: {}".format(num+1,closest[-1],row[-1])

def knn_kd(train, test, k):
    train_table = table.Table()
    train_table.add_rows(train)
    test_table = table.Table()
    test_table.add_rows(test)

    Node = collections.namedtuple("Node", 'point level left right')

    def kdtree(start, end, level = 0):
        if (start==end or level >= k):
            return None
        temp_rows = train_table.rows[start:end]
        sorted(temp_rows, key = lambda x: x[level])
        train_table.rows[start:end] = temp_rows
        me = len(temp_rows)//2
        median_point = train_table.rows[me]
        return Node(median_point, level, kdtree(start, me, level + 1), kdtree(me + 1, end, level + 1))

    tree = kdtree(0,len(train_table.rows))

    def find_closest(tree, item):
        closest = None
        if tree.point == item:
            return clos
        else:
            left = find_closest(tree.left,item)
            right = find_closest(tree.right,item)

    for num,row in enumerate(test_table.rows):
        closest = find_closest(tree, row)
        # print "{}  Actual: {} - Predicted: {}".format(num+1,closest[-1],row[-1])

    

    
def knn_mb(train, test, k, km, b, t):
    train_table = table.Table()
    train_table.add_rows(train)
    test_table = table.Table()
    test_table.add_rows(test)

    
    C = table.Table()
    C.add_rows(random.sample(train_table.rows, len(train_table.rows)))
    V = [0] * len(C.rows)       
    # C = random.sample(train_table.rows, len(train_table.rows))
    print V
    for _ in xrange(km - len(train_table.rows)): C.add_rows([[]])

    for _ in xrange(t):
        d = []
        M = table.Table()
        M.add_rows(random.sample(train_table.rows,5))
        for x in M.rows:
            d.append(C.closest_row(x))
        for x,c,i in zip(M.rows,d,xrange(len(d))):
            V[i] += 1  
            rate = 1 / V[i]
    





if __name__ == "__main__":
    # knn(sys.argv[1],sys.argv[1],1)
    # knn_mb(sys.argv[1],sys.argv[1],1, 20, 5, 100)
    knn_kd(sys.argv[1],sys.argv[1],10)

