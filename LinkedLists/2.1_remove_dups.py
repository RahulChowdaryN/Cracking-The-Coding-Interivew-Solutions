class Node:
    def __init__(self,value):
        self.val = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def remove_dups_optmzd(self):
        # O(N)
        current = self.head
        buffer = set([current.val])

        while current.next:
            if current.next.val in buffer:
                current.next = current.next.next
            else:
                buffer.add(current.next.val)
                current = current.next

    def remove_dups(self):

        current = self.head
        buffer = set()

        while current.next is not None:
            if current.val in buffer:
                current.val= current.next.val
                current.next = current.next.next
            else:
                 buffer.add(current.val)

                 current = current.next

        if current.val in buffer:

            current = None

        else:
            buffer.add(current.val)

        return True

    def remove_dups_nospace(self):
        # O(N ** 2)
        current = self.head

        while current:
            runner = current
            while runner.next:
                if runner.next.val == current.val:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next

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



a = [1,5,3,4,5,5,5,8,8]

ll = LinkedList()

for i in a:
    ll.insert_elements(i)

ll.traverse_list()
ll.remove_dups_nospace()
ll.traverse_list()