class Stack:
    def __init__(self):
        self.stack_one = []

    def push(self,item):

        temp_stack = []

        if not self.stack_one:
            self.stack_one.append(item)
            return True
        if item >= self.stack_one[-1]:
            self.stack_one.append(item)
            return True
        else:
            while self.stack_one:
                temp_value = self.stack_one[-1]
                if item >= temp_value:
                    break
                temp_stack.append(self.stack_one.pop())
            self.stack_one.append(item)
            while temp_stack:
                self.stack_one.append(temp_stack.pop())
            return True


    def peek(self):
        if self.stack_one:
            return self.stack_one[-1]

        return None

    def pop(self):
        return self.stack_one.pop()

    def is_empty(self):
        return len(self.stack_one) == 0

input = [10,2,8,5,12]

stck = Stack()

for i in input:
    stck.push(i)
print(stck.stack_one)
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