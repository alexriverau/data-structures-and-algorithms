from data_structures.invalid_operation_error import InvalidOperationError


# creates Queue class
class Queue:

    # instantiates Queue
    def __init__(self, front=None):
        self.front = front
        self.rear = None

    ''' enqueue method:
    - adds a new node to the back of the queue with an O(1) time performance'''
    def enqueue(self, value):
        node = Node(value)

        if self.front is None:
            self.front = node
            self.rear = node
        elif self.rear:
            self.rear.next = node
            self.rear = node

    ''' dequeue method:
    - returns value of the node from the front of the queue
    - removes the node from the front of the queue
    - raises exception when called on empty queue'''
    def dequeue(self):

        if self.front is None:
            raise InvalidOperationError('Method not allowed on empty collection')

        temp = self.front
        self.front = self.front.next
        temp.next = None
        return temp.value

    '''peek method:
    - returns value of the node from the front of the queue
    - raise exception when called on empty queue'''
    def peek(self):

        if self.front is None:
            raise InvalidOperationError('Method not allowed on empty collection')
        else:
            return self.front.value

    '''is_empty method:
    - returns boolean indicating whether or not the queue is empty'''
    def is_empty(self):

        if self.front is None:
            return True
        else:
            return False


# creates a Node class
class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next
