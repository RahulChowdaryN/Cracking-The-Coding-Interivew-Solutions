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

    def kth_element(self,k):
        current = self.head
        slow = fast = current
        for i in range(k):
            if not fast:
                return None
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        if not slow:
            return None
        return slow.val


a = [1,2,3,4,5,6,7,8,9]

ll = LinkedList()

for i in a:
    ll.insert_elements(i)

#print(ll.kth_element(3))

class Test(unittest.TestCase):

    def test_kth_element(self):
        self.assertEqual(8,ll.kth_element(2))
        self.assertEqual(5, ll.kth_element(5))
        self.assertEqual(9, ll.kth_element(1))
        self.assertEqual(None, ll.kth_element(12))
        self.assertEqual(None, ll.kth_element(0))

if __name__ == "__main__":
    if __name__ == '__main__':
        unittest.main()
