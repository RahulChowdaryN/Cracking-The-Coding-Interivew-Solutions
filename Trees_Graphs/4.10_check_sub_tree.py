def check_subtree(t1,t2):

    if not t2:
        return False

    if not t1:
        return False

    if t1.left == t2 and match_tree(t1.left,t2):
        return True

    if t1.right == t2 and match_tree(t1.right,t2):
        return True

    return check_subtree(t1.left,t2) or check_subtree(t1.right,t2)


def match_tree(t1,t2):
    if t1 == None and t2 == None:
        return True

    if t1 == None or t2 == None:
        return False

    if t1.data != t2.data:
        return False

    return match_tree(t1.left,t2.left) and match_tree(t1.right,t2.right)
