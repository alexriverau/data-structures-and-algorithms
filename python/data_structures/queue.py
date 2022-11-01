# creates Queue class
class Queue:
    """
    Put docstring here
    """

    # instantiates Queue
    def __init__(self, front=None):
        self.front = front

    # enqueue method
    def enqueue(self, value):
        pass

    # dequeue method
    def dequeue(self):
        pass

    # peek method
    def peek(self):
        pass

    # is_empty method
    def is_empty(self):
        pass


# creates a Node class
class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next
