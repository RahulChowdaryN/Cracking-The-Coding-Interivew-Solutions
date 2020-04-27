class Node:
    def __init__(self,data,left = None,right = None):
        self.root = data
        self.left = left
        self.right = right
        self.parent = None

        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self

def successor(node):
    if not node:
        return None

    child = node.right

    if node.right:
        while child.left:
            child = child.left

    if child:
        return child

    if node.parent and node.parent.data > node.data:
        return node.parent

    return None

