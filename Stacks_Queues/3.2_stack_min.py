class Stack:

    def __init__(self):
        self.min = None
        self.stack = []

    def push(self,item):
        self.mini(item)
        self.stack.append((item,self.min))
        return True

    def pop(self):
        item = self.stack.pop()
        return item[0]

    def mini(self,item = None):
        if item == None:
            if self.stack:
                return self.stack[-1][1]
            return None
        if self.min == None:
            self.min = item
            return
        self.min = self.stack[-1][1]
        if self.min > item:
            self.min = item


import unittest

class Test(unittest.TestCase):
  def test_min_stack(self):
    min_stack = Stack()
    self.assertEqual(min_stack.mini(), None)
    min_stack.push(7)
    self.assertEqual(min_stack.mini(), 7)
    min_stack.push(6)

    min_stack.push(5)

    self.assertEqual(min_stack.mini(), 5)
    min_stack.push(10)
   # min_stack.push(3)
    print(min_stack.stack)

    self.assertEqual(min_stack.mini(), 5)
    self.assertEqual(min_stack.pop(), 10)
    self.assertEqual(min_stack.pop(), 5)

    self.assertEqual(min_stack.mini(), 6)
    self.assertEqual(min_stack.pop(), 6)
    self.assertEqual(min_stack.pop(), 7)
  #  self.assertEqual(min_stack.min, None)

if __name__ == "__main__":
  unittest.main()


import schedule