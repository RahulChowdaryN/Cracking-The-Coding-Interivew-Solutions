import unittest
class Node:
    def __init__(self,value):
        self.val = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_elements(self,value):
        new_node = Node(value)
        current = self.head

        if current is None:
            self.head = new_node
        else:
            while current.next is not None:
                current = current.next
            current.next = new_node

    def traverse_list(self):
        current = self.head
        print("traversing")

        while current is not None:
            print("\n",current.val,end=" ")
            current = current.next

def intersection(l1,l2):
    if l1 == l2:
        return True
    if not l1 and not l2:
        return False
    if not l1 or not l2:
        return False

    len_l1 = 0
    len_l2 = 0

    while l1:
        len_l1 +=1
        l1 = l1.next

    while l2:
        len_l2 +=1
        l2 = l2.next

    if l1 != l2:
        return False

    if len_l1 > len_l2:
        diff = len_l1 - len_l2
        for i in range(diff):
            l1 = l1.next
    else:
        diff = len_l2 - len_l1
        for i in range(diff):
            l2 = l2.next

    while l1 and l2:
        if l1 == l2:
            return l1
        l1 = l1.next
        l2 = l2.next



a = [1,2,3,4,5,6,7,8,9]

ll = LinkedList()

for i in a:
    ll.insert_elements(i)

