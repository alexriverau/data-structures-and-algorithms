class Node:
    """
    Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.
    """

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    """
    Create a Binary Tree class
    Define a method for each of the depth first traversals:
    - pre order
    - in order
    - post order
    Each depth first traversal method should return an array of values, ordered appropriately.
    """

    def __init__(self, root=None):
        self.root = root

    def pre_order(self, values=[]):
        # root >> left >> right

        # helper function that moves to nodes in pre_order order and appends values to list
        def walk(input_node, lst_values):
            # check if tree is empty
            if not input_node:
                return
            # append root value to list
            lst_values.append(input_node.value)
            # walk to left node and repeat process to append value to list by calling walk function
            walk(input_node.left, lst_values)
            # walk to right node and repeat process to append value to list by calling walk function
            walk(input_node.right, lst_values)

        # invoke helper function passing root node and list of values
        walk(self.root, values)
        return values

    def in_order(self, values=[]):
        # left >> root >> right

        # helper function that moves to nodes in in_order order and appends values to list
        def walk(input_node, lst_values):
            # check if tree is empty
            if not input_node:
                return

            # walk to left node and repeat process to append value to list by calling walk function
            walk(input_node.left, lst_values)
            # append root value to the list
            lst_values.append(input_node.value)
            # walk to right node and repeat process to append value to list by calling walk function
            walk(input_node.right, lst_values)

        # invoke helper function passing root node and list of values
        walk(self.root, values)
        return values

    def post_order(self, values=[]):
        # left >> right >> root

        # helper function that moves to nodes in in_order order and appends values to list
        def walk(input_node, lst_values):
            # check if tree is empty
            if not input_node:
                return

            # walk to left node and repeat process to append value to list by calling walk function
            walk(input_node.left, lst_values)
            # walk to right node and repeat process to append value to list by calling walk function
            walk(input_node.right, lst_values)
            # append root value to the list
            lst_values.append(input_node.value)

        walk(self.root, values)
        return values

    # def find_maximum_value(self):
    #     if not self.root:
    #         return 'binary tree empty'
    #
    #     lst_values = self.pre_order()
    #     max_val = 0
    #
    #     # iterate over pre_order list
    #     for val in lst_values:
    #         if val > max_val:
    #             max_val = val
    #     return max_val
