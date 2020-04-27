class Bstree:
    def __init__(self,val):
        self.root = val
        self.left = None
        self.right = None

    def insert(self,item):

        if not item:
            return None

        if not self.root:
            self.root = Bstree(item)

        if item < self.root:
            if self.left:
                return self.left.insert(item)
            else:
                self.left = Bstree(item)
                return True

        else:
            if self.right:
                return self.right.insert(item)
            else:
                self.right  = Bstree(item)
                return  True

    def preorder(self):
        print(self.root)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.root)
        if self.right:
            self.right.inorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()

        print(self.root)

arr = [1,2,3,4,5,6,7,8]
middle = len(arr) // 2
r = Bstree(arr[middle-1])
for item in arr:
    if item == arr[middle-1]:
        continue
    r.insert(item)
# r.insert(30)
# r.insert(20)
# r.insert(40)
# r.insert(70)
# r.insert(60)
# r.insert(80)
print("preorder")
r.preorder()
print("postorder")
r.postorder()
print("inorder")
r.inorder()
