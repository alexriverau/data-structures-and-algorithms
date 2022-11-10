from data_structures.stack import Stack


class PseudoQueue:

    def __init__(self):
        self.stack = Stack()
        self.temp = Stack()

    def enqueue(self, value):
        while not self.temp.is_empty():
            self.stack.push(self.temp.pop())
        self.stack.push(value)
        return self.stack

    def dequeue(self):
        if self.stack is not None:

            while not self.stack.is_empty():
                self.temp.push(self.stack.pop())
        return self.temp.pop()
