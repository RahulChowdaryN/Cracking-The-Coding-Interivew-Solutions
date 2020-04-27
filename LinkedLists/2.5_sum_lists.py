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
        temp = current = self.head
        print("traversing")

        while current is not None:
            print("\n",current.val,end=" ")
            current = current.next

        return temp

def sum_lists(l1,l2):
    #total = 0
    carry = 0
    temp = l3 = Node(None)
    while l1 or l2 or carry:
        if l1:
            first = l1.val
            l1 = l1.next
        else:
            first = 0
        if l2:
            second = l2.val
            l2 = l2.next
        else:
            second  = 0

        total = first + second + carry
        carry = total // 10
        l3.next = Node(total%10)
        l3 = l3.next
   # if carry:
    #    l3.next = Node(carry)
    return temp.next

def sum_lists_follow_up(l1, l2):
    # total = 0
    carry = 0
    temp = l3 = Node(None)
    result = 0
    while l1 and l2:
        if l1:
            first = l1.val
            l1 = l1.next
        else:
            first = 0
        if l2:
            second = l2.val
            l2 = l2.next
        else:
            second =0

        result = (result * 10) + first + second
        

    #    print(result)

    ll = LinkedList()
    for i in str(result):
        ll.insert_elements(i)
    ll.traverse_list()



# if carry:
#    l3.next = Node(carry)









a = [6,1,7]
b = [2,9,5
      ]

l1 = LinkedList()
l2 = LinkedList()

for i in a:
    l1.insert_elements(i)
for i in b:
    l2.insert_elements(i)

l11 = l1.traverse_list()
l22 = l2.traverse_list()
response = sum_lists(l11,l22)

print("sum")
while response is not None:
    print(response.val)
    response = response.next
print("follow up")
sum_lists_follow_up(l11,l22)
# sudo apt-get purge --auto-remove elasticsearch
#  hosts: ['10.0.0.63']:9200