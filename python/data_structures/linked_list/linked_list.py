# creates Linked List class
class LinkedList:

    # instantiates Linked List
    def __init__(self, head=None):
        self.head = head

    # insert method
    def insert(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        elif self.head is not None:
            node.next = self.head
            self.head = node

    # includes method
    def includes(self, value):
        current = self.head

        while current is not None:
            if current.value == value:
                return True
            current = current.next

    # to string method
    def __str__(self):
        string = ''
        current = self.head

        while current is not None:
            string += f'{{ {current.value} }} -> '
            print(string)
            current = current.next
        string += 'None'
        print(string)
        return string


# creates Node class
class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next
