from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    Create a Binary Search Tree class. It should be a sub-class of the Binary Tree Class, with the following additional methods:
    - Add
        Arguments: value
        Return: nothing
        Adds a new node with that value in the correct location in the binary search tree.
    - Contains
        Argument: value
        Returns: boolean indicating whether or not the value is in the tree at least once.
    """

    def __init__(self, root=None):
        self.root = root

    def add(self, value):
        node = Node(value)

        # check if tree is empty
        if not self.root:
            self.root = node
            return

        root = self.root

        # traverse over tree
        while root:
            # check values left side and adds new node
            if value < root.value:
                if root.left:
                    root = root.left
                else:
                    root.left = node
                    return

            # check values right side and adds new node
            if value > root.value:
                if root.right:
                    root = root.right
                else:
                    root.right = node
                    return

    def contains(self, value):
        root = self.root

        # traverse over tree
        while root:
            # check if value is the same as the root
            if value == root.value:
                return True

            # check values left side
            if value < root.value:
                root = root.left

            # check values right side
            if value > root.value:
                root = root.right

        return False
