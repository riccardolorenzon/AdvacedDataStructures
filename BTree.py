class Person(object):
    def __init__(self, priority, name):
        self.priority = priority
        self.name = name
    def __str__(self):
        return "NAME : %s, Priority : %d" % (self.priority, self.name)

class node(object):
    def __init__(self, value, leftChild, rightChild):
        if leftChild == None and rightChild == None:
            #leaf scenario
            self.value = value
            self.left = None
            self.right = None
        else:
            #node scenario
            self.value = value
            if leftChild != None:
                self.left = node(leftChild, None, None)
            else:
                self.left = None
            if rightChild != None:
                self.right = node(rightChild, None, None)
            else:
                self.right = None

    def findNode(self, person):
        if self.value.name == person.name:
            return self
        else:
            if self.left != None:
                nodeFound = self.left.findNode(person)
            if self.right != None:
                nodeFound = self.right.findNode(person)
            return nodeFound

    def insert(self, parent, value):
        nodeFound = self.findNode(parent)
        if nodeFound == None:
            print "impossibile trovare %s" % parent.name
            return
        if nodeFound.left == None:
            nodeFound.left = node(value, None, None)
        else:
            if nodeFound.right == None:
                nodeFound.right = node(value, None, None)
            else:
                raise BaseException("max 2 sub employees for each supervisor")
#first line
line = raw_input()
sup = line.split("->")[0]
emp = line.split("->")[1]
tree= node(Person("-1", sup.strip()), Person("-1", emp.strip()), None)

sentinel = '' # ends when this string is seen
for line in iter(raw_input, sentinel):
    sup = line.split("->")[0]
    emp = line.split("->")[1]
    supNode = Person("-1", sup.strip())
    empNode = Person("-1", emp.strip())
    tree.insert(supNode, empNode)

l = []
l = [tree]

while len(l) != 0:
    x = l.pop()
    print x.value.name
    if x.left != None:
        l.append(x.left)
    if x.right != None:
        l.append(x.right)
