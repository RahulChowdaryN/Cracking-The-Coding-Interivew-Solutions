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

    def partition(self,k):
        current = self.head
        temp1 = before = Node(None)
        temp2 = after = Node(None)
        while current:
            if current.val < k:
                before.next = current
                before = before.next
            else:
                after.next = current
                after = after.next
            current = current.next

        after.next = None  ##Important

        before.next = temp2.next

        return temp1.next


a = [7,2,9,1,6,3,8]

ll = LinkedList()

for i in a:
    ll.insert_elements(i)

print(ll.traverse_list())

response = ll.partition(6)

while response is not None:
    print(response.val)
    response = response.next
# sudo apt-get purge --auto-remove elasticsearch
#  hosts: ['10.0.0.63']:9200