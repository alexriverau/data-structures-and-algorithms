from data_structures.invalid_operation_error import InvalidOperationError


# creates Stack class
class Stack:

    # instantiates Stack
    def __init__(self, top=None):
        self.top = top

    ''''push method:
    - adds a new node to the top of the stack with an O(1) time performance'''
    def push(self, value):
        node = Node(value)

        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node

    '''pop method:
    - returns value of the node from the top of the stack
    - removes the node from the top of the stack
    - raises exception when called on empty stack'''
    def pop(self):

        if self.top is None:
            raise InvalidOperationError('Method not allowed on empty collection')

        temp = self.top
        self.top = self.top.next
        temp.next = None
        return temp.value

    '''peek method:
    - returns value of the node from he top of the stack
    - raises exception when called on empty stack'''
    def peek(self):

        if self.top is None:
            raise InvalidOperationError('Method not allowed on empty collection')
        else:
            return self.top.value

    '''is_empty method:
    - returns a boolean indicating whether or not the stack is empty'''
    def is_empty(self):

        if self.top is None:
            return True
        else:
            return False


# creates Node class
class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next
