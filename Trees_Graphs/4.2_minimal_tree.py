class Bstree:
    def __init__(self,val):
        self.root = val
        self.left = None
        self.right = None

    def inorder(self):
        print("inorder")
        if self.left:
            self.left.inorder()
        print(self.root)
        if self.right:
            self.right.inorder()

def minimal_tree(array):

    if not array:
        return None

    middle = len(array) // 2

    root = Bstree(array[middle ])

    root.left = minimal_tree(array[:middle ])

    root.right = minimal_tree(array[middle+1:])

    return root



def inorder(root):

    if root.left:
        inorder(root.left)
    print(root.root)
    if root.right:
        inorder(root.right)


array = [1,2,3,4,5,6,7,8]
response = minimal_tree(array)

inorder(response)