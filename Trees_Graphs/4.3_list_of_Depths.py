from collections import deque

class Node:
    def __init__(self,item):
        self.val = item
        self.next = None
class Tree:
    def __init__(self,value):
        self.root = value
        self.left = None
        self.right = None

    def insertLeft(self,value):

        new_node = Tree(value)

        if not self.left:
            self.left = new_node
            return True
        new_node.left = self.left
        self.left = new_node

    def insertRight(self,value):

        new_node = Tree(value)

        if not self.right:
            self.right = new_node
            return True

        new_node.right = self.right
        self.right = new_node


    def getRootVal(self):
        return self.root

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def setRootVal(self,value):
        if self.root:
            self.root = value
            return True
        return False


    def levelorder_iterative(self ,root):
        level = 0
        response = []
        stack = [(root ,level)]

        while stack:
            node ,level = stack.pop()

            if len(response) == level:
                new_node = Node(node.root)
                response.append([new_node])
            else:
                new_node.next = Node(node.root)
                response[level].append(new_node.next)

            if node.right:
                stack.append((node.right ,level +1))
            if node.left:
                stack.append((node.left ,level +1))
        print(response)
        return response


f = Tree('25')
f.insertLeft('15')
f.insertRight('50')
f.getLeftChild().insertLeft('10')
f.getLeftChild().insertRight('22')
f.getLeftChild().getLeftChild().insertLeft('4')
f.getLeftChild().getLeftChild().insertRight('12')
f.getLeftChild().getRightChild().insertRight('24')
f.getLeftChild().getRightChild().insertLeft('18')
f.getRightChild().insertLeft('35')
f.getRightChild().insertRight('70')
f.getRightChild().getLeftChild().insertLeft('31')
f.getRightChild().getLeftChild().insertRight('44')
f.getRightChild().getRightChild().insertLeft('66')
f.getRightChild().getRightChild().insertRight('90')
print("*********")

result = f.levelorder_iterative(f)

for node in result:
    print("level")
    for val in node:
        print(val.val)