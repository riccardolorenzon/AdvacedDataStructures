class DisjointSet(object):
    def __init__(self, n):
        '''
        initialize the array as a singleton array
        :param n:
        :return:
        '''
        self.id = [] * n
        for i in xrange(0,n):
            self.id[i] = i

    def connected(self, p,q):
        return self.id[p] == self.id[q]

    def add(self, p, q):
        pid = self.id[p]
        qid = self.id[q]
        for i in xrange(0, len(self.id)):
            if self.id[i] == pid:
                self.id[i] = qid

    def show(self):
        out = ""
        for i in xrange(0, len(self.id)):
            out += self.id[i]
            if i < len(self.id) -1:
                out += ' '
        print out

if __name__ == '__main__':
    disjointSet = DisjointSet(10)
    #0-5 3-0 6-0 9-0 8-4 7-9
    disjointSet.add(0,5)
    disjointSet.add(3,0)
    disjointSet.add(6,0)
    disjointSet.add(9,0)
    disjointSet.add(8,4)
    disjointSet.add(7,9)
    disjointSet.show()

    #1-0 6-2 9-8 0-2 8-3 3-4 4-5 7-6 9-2

    disjointSet = DisjointSet(10)
    disjointSet.add(1,0)
    disjointSet.add(6,2)
    disjointSet.add(9,8)
    disjointSet.add(0,2)
    disjointSet.add(8,3)
    disjointSet.add(3,4)
    disjointSet.add(4,5)
    disjointSet.add(7,6)
    disjointSet.add(9,2)
    disjointSet.show()
