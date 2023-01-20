from data_structures.binary_tree import BinaryTree
from data_structures.hashtable import Hashtable


def tree_intersection(tree1, tree2):
    hashmap = Hashtable()
    intersection = []

    if not tree1.root and not tree2.root:
        return intersection

    def add_to_hashmap(node):
        if node:
            hashmap.set(node.value, True)
            add_to_hashmap(node.left)
            add_to_hashmap(node.right)

    add_to_hashmap(tree1.root)

    def add_to_intersection(node):
        if node:
            if hashmap.get(node.value):
                intersection.append(node.value)
            add_to_intersection(node.left)
            add_to_intersection(node.right)
    add_to_intersection(tree2.root)

    return intersection
