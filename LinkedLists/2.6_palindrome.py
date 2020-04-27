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

    def palindrome(self):
        current = self.head
        fast = slow = current
        prev = None

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        print(slow.val)
        while slow:
            nextt = slow.next
            slow.next = prev
            prev = slow
            slow = nextt

        while current and prev:
            print(current.val,prev.val)

            if current.val != prev.val:
                return False
            current = current.next
            prev = prev.next
        return True




a = [1,2,3,4,5,1,6]

ll = LinkedList()

for i in a:
    ll.insert_elements(i)

print(ll.palindrome())

