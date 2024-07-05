'''
TODO:
        A pickle file containing a single serialized function is given.

        Write a program that calls this function with the given arguments and
        prints the return value of the function.

        The program receives the name of the pickle file containing the single
        serialized function as its first input line.

        Then an arbitrary number of lines are passed, each containing a
        positional argument for this function.

        The program must call the function from the specified pickle file with
        all the string arguments entered, and print the return value of
        the function.

        The arguments must be passed in the order in which they were entered.

NOTE:
        The arguments passed to the function must be of type str.

        Let's look at the first test.

        First, the name of the file is passed — func.pkl, which contains the
        serialized function:
            def func(*args):
            return ' '.join(args)
        then the arguments for this function:
            Hello,, how, are, you and today?.

        The program prints the result of the following call:
            func('Hello,', 'how', 'are', 'you', 'today?')

        To read an arbitrary number of lines, use the sys.stdin stream input.

        Assume that the input file is in the program folder.

        This task implements two functions behind the scenes, named func
        and add.

        Do not use these names for your variables to avoid errors.
'''
import sys
import pickle
from typing import List, Callable


def read_input(input_stream=sys.stdin) -> List[str]:
    """
    Reads input from the given input stream and returns a list of
    stripped lines.
    """
    return [line.strip() for line in input_stream.readlines()]


def deserialize_pickle(pickle_filepath: str) -> Callable:
    """
    Deserializes a function from the given pickle file.

    Args:
        pickle_filepath (str): Path to the pickle file.

    Returns:
        Callable: The deserialized function.
    """
    with open(pickle_filepath, 'rb') as file:
        return pickle.load(file)


def call_func_from_pickle(pickle_filepath: str, arguments: List[str]) -> str:
    """
    Calls a function from the given pickle file with the provided arguments.

    Args:
        pickle_filepath (str): Path to the pickle file.
        arguments (List[str]): List of arguments to pass to the function.

    Returns:
        str: The return value of the function call.
    """
    loaded_function = deserialize_pickle(pickle_filepath)
    return loaded_function(*arguments)


# Main execution block
if __name__ == "__main__":
    # Read the pickle file name from input
    pickle_filename = input().strip()

    # Read the function arguments from input
    arguments = read_input()

    # Call the function and print the result
    print(call_func_from_pickle(pickle_filename, arguments))
