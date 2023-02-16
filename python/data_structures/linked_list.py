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

    # kth from end method
    def kth_from_end(self, k):
        length = 0
        current = self.head

        while current is not None:
            length += 1
            current = current.next

        target = length-k

        if k >= length:
            raise Exception
        if target == 0:
            return self.head.value

        current = self.head

        for i in range(target - 1):
            current = current.next

        return current.value

    def add(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = node

    def reverse(self):
        if not self.head:
            return

        previous = None
        current = self.head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous

    def ll_add_one(self):
        self.reverse()
        current = self.head

        while current:
            if current.value == 9 and current.next:
                current.value = 0
                current = current.next

            elif current.value < 9:
                current.value += 1
                break

            else:
                current.value = 0
                node = Node(1)
                current.next = node
                break
        self.reverse()


# creates Node class
class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# create Target Error class
class TargetError:
    pass
