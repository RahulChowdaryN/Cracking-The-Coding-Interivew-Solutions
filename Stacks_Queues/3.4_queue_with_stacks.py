class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def add(self,item):
        self.stack1.append(item)
        return True


    def remove(self):
        if self.stack2:
            item = self.stack2.pop()
            return item
        if not self.stack1:
            return None
        while self.stack1:
            item = self.stack1.pop()
            self.stack2.append(item)
        return self.stack2.pop()

    def peek(self):
        if self.stack2:
            return self.stack2[-1]
        if self.stack1:
            return self.stack1[-1]
        return False

    def isEmpty(self):
        return self.stack1 + self.stack2 == 0

