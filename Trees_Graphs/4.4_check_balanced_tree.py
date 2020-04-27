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

    def tree_level(self,root):

        if root is None:
            return 0

        lDepth = self.tree_level(root.left)
        rDepth = self.tree_level(root.right)

        diff = lDepth - rDepth

        if abs(diff) > 1:
            return -2

        return max(lDepth,rDepth) + 1


    def check_balanced(self,root):
        if not self.root:
            return True



        left = self.tree_level(self.left)
        if left == -2:
            return False

        right = self.tree_level(self.right)

        if right == -2:
            return False

        if abs(left - right) > 1:
            return False
        return True