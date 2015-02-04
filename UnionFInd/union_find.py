class QuickUnionFind(object):
    def __init__(self, n):
        '''
        initialize the array as a singleton array
        :param n:
        :return:
        '''
        self.id = [0] * n
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
            out += str(self.id[i])
            if i < len(self.id) -1:
                out += ' '
        print out

class QuickUnionWeightedUF:
    def __init__(self, n):
        self.id = [0] * n
        self.sz = [0] * n
        for i in xrange(0,n):
            self.id[i] = i
            self.sz[i] = 1

    def root(self,i):
        while i != self.id[i]:
            i = self.id[i]
        return i

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def add(self, p, q):
        i = self.root(p)
        j = self.root(q)
        if i == j:
            return
        if self.sz[i] < self.sz[j]:
            self.id[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]
        self.show()

    def show(self):
        out = ""
        for i in xrange(0, len(self.id)):
            out += self.id[i].__str__()
            if i < len(self.id) - 1:
                out += ' '
        print out
    """

    public void show() {
        String out = "";
        for( int i=0; i<id.length; i++) {
            out += id[i];
            if(i < id.length - 1 ) out += " ";
        }
        System.out.println(out);
    }
}
"""





if __name__ == '__main__':
    # 6-8 7-1 2-0 0-9 6-0 3-5
    disjointSet = QuickUnionFind(10)
    disjointSet.add(6,8)
    disjointSet.add(7,1)
    disjointSet.add(2,0)
    disjointSet.add(0,9)
    disjointSet.add(6,0)
    disjointSet.add(3,5)
    disjointSet.show()
    #4-3 0-2 1-9 6-7 2-1 8-6 4-6 9-6 1-5
    quickdisjointSet = QuickUnionWeightedUF(10)
    quickdisjointSet.add(4,3)
    quickdisjointSet.add(0,2)
    quickdisjointSet.add(1,9)
    quickdisjointSet.add(6,7)
    quickdisjointSet.add(2,1)
    quickdisjointSet.add(8,6)
    quickdisjointSet.add(4,6)
    quickdisjointSet.add(9,6)
    quickdisjointSet.add(1,5)
    quickdisjointSet.show()