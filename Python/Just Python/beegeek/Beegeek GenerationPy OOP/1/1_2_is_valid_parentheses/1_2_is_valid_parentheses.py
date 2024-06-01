'''
TODO:
        Let's call a bracket sequence a string consisting of the
        characters ( and ).

        We will consider a bracket sequence correct if:
            - for each opening bracket there is a closing bracket
            - brackets are closed in the correct order, that is, in each
            pair of opening and closing brackets, the opening one is to
            the left

        Write a program that determines whether a bracket sequence is
        correct.

        Input:
            The program receives a string representing a bracket
            sequence as input.

        Output:
            The program should output True if the input bracket sequence
            is correct, or False otherwise.
'''


def is_valid_parentheses(bracket_sequence: str) -> bool:
    # Dictionary for matching opening and closing parentheses
    bracket_map = {')': '(', ']': '[', '}': '{'}
    # Stack for storing opening parentheses
    stack: list[str] = []

    open_brackets = bracket_map.values()
    close_brackets = bracket_map.keys()

    for char in bracket_sequence:
        if char in open_brackets:
            stack.append(char)
        elif char in close_brackets:
            if stack == [] or stack.pop() != bracket_map[char]:
                return False

    # Check that all opening parentheses have been closed
    return not stack


if __name__ == "__main__":
    input_string = input()
    print(is_valid_parentheses(input_string))
