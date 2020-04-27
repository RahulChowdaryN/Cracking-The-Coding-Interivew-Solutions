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

    def middle_element(self):
        current = self.head
        slow = fast = current
        if not fast.next.next:
            return None
        while fast and fast.next and fast.next.next:
            slow=slow.next
            fast = fast.next.next
        print(slow.val)
        if slow is None:
            return None
        slow.val = slow.next.val
        slow.next = slow.next.next

        return current


a = [1,2]

ll = LinkedList()

for i in a:
    ll.insert_elements(i)

print(ll.traverse_list())
ll.middle_element()
#class Test(unittest.TestCase):

#    def test_kth_element(self):
#        self.assertEqual(8,ll.middle_element())

print(ll.traverse_list())
# if __name__ == "__main__":
#     if __name__ == '__main__':
#         unittest.main()
