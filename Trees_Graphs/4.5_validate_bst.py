#recursive

class Tree:
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None
def validate_bst(root,low = float('-inf'),high = float('inf')):

    if not root:
        return True

    value = root.val

    if value <= low or value >= high:
        return False

    if not validate_bst(root.left,low,value):
        return False

    if not validate_bst(root.right,value,high):
        return False

    return True

root = Tree(12)

print(validate_bst(root))

#iterative

#Inorder

def validate_bst_itr(root):
    stack = []
    prev = float('-inf')
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        elif stack:
            root  = stack.pop()

            if not root.val > prev:
                return False
            root = root.right
    return True









