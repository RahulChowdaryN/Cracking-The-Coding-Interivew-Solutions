class Stack_Plates:
    def __init__(self):
        self.threshold = 3
        self.counter = 0
        self.stack_dict = {}

    def push(self,item):
        if len(self.stack_dict) == 0:
            self.stack_dict[self.counter] = [item]
            return True

        if len(self.stack_dict[self.counter]) <self.threshold:
            self.stack_dict[self.counter].append(item)
            return True
        else:
            self.counter += 1
            self.stack_dict[self.counter] = [item]
            return True

    def pop(self):
        if len(self.stack_dict) == 0:
            return None

        if len(self.stack_dict[self.counter] ) == 0:
            del self.stack_dict[self.counter]
            self.counter -=1

        if self.counter >= 0:
            item = self.stack_dict[self.counter].pop()
            print(self.stack_dict)
            return item

        return None

    # def pop_at(self,index):
    #     if index < 0



# stack = Stack_Plates()
#
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.pop()
# stack.push(4)
# stack.pop()
# stack.push(5)
# stack.push(6)
# stack.push(7)
# stack.push(8)
# stack.pop()
# stack.pop()
# stack.pop()
# stack.pop()

import unittest

class Test(unittest.TestCase):
  def test_multi_stack(self):
    stack = Stack_Plates()
    stack.push(11)
    stack.push(22)
    stack.push(33)
    stack.push(44)
    stack.push(55)
    stack.push(66)
    stack.push(77)
    stack.push(88)
    self.assertEqual(stack.pop(), 88)
  #  self.assertEqual(stack.pop_at(1), 66)
  #  self.assertEqual(stack.pop_at(0), 33)
  #  self.assertEqual(stack.pop_at(1), 55)
  #  self.assertEqual(stack.pop_at(1), 44)
  #  self.assertEqual(stack.pop_at(1), None)
    stack.push(99)
    self.assertEqual(stack.pop(), 99)
    self.assertEqual(stack.pop(), 77)
    self.assertEqual(stack.pop(), 66)
    self.assertEqual(stack.pop(), 55)
   # self.assertEqual(stack.pop(), None)

if __name__ == "__main__":
  unittest.main()