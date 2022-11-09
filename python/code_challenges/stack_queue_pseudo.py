from data_structures.stack import Stack


class PseudoQueue:

    def __init__(self):
        self.stack = Stack()
        self.temp = Stack()

    def enqueue(self, value):
        while self.temp is not None:
            self.stack.push(self.temp.pop())
        self.stack.push(value)

    def dequeue(self):
        if self.stack is None:
            return None

        while self.stack is not None:
            self.temp.push(self.stack.pop())

        return self.temp.pop()
