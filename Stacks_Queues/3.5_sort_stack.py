class Stack:
    def __init__(self):
        self.stack_one = []
        self.temp_stack= []

    def push(self,item):

        if not self.stack_one:
            self.stack_one.append(item)
            return True
        minimum = self.peek()
        if item <= minimum:
            self.stack_one.append(item)
            return True

        while self.stack_one and item >= minimum:
            minimum = self.stack_one.pop()
            if item <= minimum:
                self.stack_one.append(minimum)
                break
            self.temp_stack.append(minimum)

        self.stack_one.append(item)
        while self.temp_stack:
            num_insert = self.temp_stack.pop()
            self.stack_one.append(num_insert)
        return True

    def peek(self):
        if self.stack_one:
            return self.stack_one[-1]

        return None

    def pop(self):
        return self.stack_one.pop()

    def is_empty(self):
        return len(self.stack_one) == 0

input = [34, 3, 31, 98, 92, 23]

stck = Stack()

for i in input:
    stck.push(i)

while not stck.is_empty():
    item = stck.pop()
    print(item)
# import unittest
#
# class Test(unittest.TestCase):
#   def test_sort_stack(self):
#   #  self.assertEqual(str(sort_stack(Stack())), "None,None")
#     stack = Stack()
#     stack.push(10)
#     stack.push(30)
#     stack.push(70)
#     stack.push(40)
#     stack.push(80)
#     stack.push(20)
#     stack.push(90)
#     stack.push(50)
#     stack.push(60)
#     self.assertEqual(stack.pop(), 10)
#     self.assertEqual(stack.pop(), 20)
#
#     self.assertEqual(stack.pop(), 30)
#     self.assertEqual(stack.pop(), 40)
#     self.assertEqual(stack.pop(), 50)
# if __name__ == "__main__":
#   unittest.main()