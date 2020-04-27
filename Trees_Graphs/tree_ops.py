from collections import deque
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

    def inorder(self):

        if self.left:
            self.left.inorder()
        print(self.root,end= " ")
        if self.right:
            self.right.inorder()




    def preorder(self):

        print( self.root , end= " " )

        if self.left:
            self.left.preorder()

        if self.right:
            self.right.preorder()



    def postorder(self):
        if self.left:
            self.left.postorder()

        if self.right:
            self.right.postorder()

        print(self.root, end = " ")

    def preorder_iterative(self,root):

        stack = [root]

        print("\t")

        while stack:
            node = stack.pop()
            print(node.root, end = " ")
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return

    def inorder_iterative(self,root):
        print("\t")

        stack = []

        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            elif stack:
                root = stack.pop()
                print(root.root, end= " ")
                root = root.right

    def postorder_iterative(self,root):
        stack1 = [root]
        stack2 = []
        print("\t")
        while stack1:
            node = stack1.pop()
            stack2.append(node.root)

            if node.left:
                stack1.append(node.left)

            if node.right:
                stack1.append(node.right)

        while stack2:
            print(stack2.pop(),end = " ")


    def tree_level(self,root):

        if root is None:
            return 0

        lDepth = self.tree_level(root.left)
        rDepth = self.tree_level(root.right)

        if lDepth > rDepth:
            return lDepth  + 1
        else:
            return rDepth + 1

    def levelorder_iterative(self,root):
        level = 0
        response = []
        stack = [(root,level)]

        while stack:
            node,level = stack.pop()
            if len(response) == level:
                response.append([node.root])
            else:
                response[level].append(node.root)

            if node.right:
                stack.append((node.right,level+1))
            if node.left:
                stack.append((node.left,level+1))
        print(response)
        return
    def level(self):
        pass

    def zigzag(self,root):

        queue = deque([(root, 0)])
        response = []

        while queue:
            node , depth  = queue.pop()
            if len(response) == depth:
                response.append([node.root])
            else:
                if depth % 2 == 0:
                    response[depth] = [node.root] + response[depth]
                else:
                    response[depth]= response[depth] + [node.root]
            if node.right:
                queue.appendleft((node.right,depth + 1))
            if node.left:
                queue.appendleft((node.left,depth + 1))
        return response

    def max_number(self,root):

        stack = [root]
        maxim = root.root
        print("maxi",maxim)
        while stack:
            node = stack.pop()
            if node.root > maxim:
                maxim = node.root
            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)
        return maxim

    def max_recursion(self,start):

        if start == None:
            return False

        res = start.root
        left = self.max_recursion(start.left)
        right = self.max_recursion(start.right)

        if left > right:
            res = left
        elif right > left:
            res = right
        return res

    def min_number(self,root):
        stack = [root]
        maxim = root.root
        while stack:
            node = stack.pop()
            if int(maxim) > int(node.root):
                maxim = node.root
            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)
        return maxim

    
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
print("In order")
f.inorder()
f.inorder_iterative(f)
print("\npreorder")
f.preorder()
f.preorder_iterative(f)

print("\npost order")
f.postorder()
f.postorder_iterative(f)

print("\nLevel Order")
f.levelorder_iterative(f)
print(f.tree_level(f))
print(f.zigzag(f))
print(f.max_number(f))
print(f.max_recursion(f))
print(f.min_number(f))