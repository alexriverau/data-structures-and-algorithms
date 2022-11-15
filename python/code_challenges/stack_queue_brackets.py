from data_structures.stack import Stack


def multi_bracket_validation(string):
    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']
    balanced_brackets = {'(': ')', '[': ']', '{': '}'}
    stack = Stack()

    for char in string:
        if char in opening_brackets:
            stack.push(char)
        elif stack.is_empty():
            return False
        elif char in closing_brackets:
            if balanced_brackets[stack.pop()] != char:
                return False

    return True
