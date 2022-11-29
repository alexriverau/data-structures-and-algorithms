from data_structures.binary_tree import BinaryTree
from data_structures.queue import Queue


def breadth_first(tree):
    queue = Queue()
    list_values = []

    if tree.root:
        queue.enqueue(tree.root)

    while not queue.is_empty():
        node = queue.dequeue()
        list_values.append(node.value)

        if node.left:
            queue.enqueue(node.left)
        if node.right:
            queue.enqueue(node.right)
    return list_values
