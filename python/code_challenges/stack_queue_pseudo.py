from data_structures.stack import Stack


class PseudoQueue:

    def __init__(self):
        self.stack = Stack()
        self.temp = Stack()

    def enqueue(self, value):
        self.stack.push(value)

    def dequeue(self):
        pass

