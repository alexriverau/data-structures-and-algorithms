from data_structures.stack import Stack


class PseudoQueue:

    def __init__(self):
        self.stack = Stack()
        self.temp = Stack()

    def enqueue(self, value):
        self.stack.push(value)

    def dequeue(self):
        if self.stack is None:
            return None

        while self.stack:
            pop_stack_val = self.stack.pop()
            push_temp_val = self.temp.push(pop_stack_val)

        while self.temp:
            pop_temp = self.temp.pop()
            self.stack.push(pop_temp)

        return push_temp_val

