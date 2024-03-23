'''
TODO:
        The function takes as arguments the start and end value of the range and an indefinite number of numbers to check.

        Write a function that will return a list of numbers that fall within a specified range.

        If the value is out of range, the function should print the message "Number out of range."

        Add the test_range() function so that it:
            - accepted as arguments
            - start and end value of the range,
            - an indefinite number of numbers to check;

            - formed a list of numbers that fall within the established range;
            - for values that are outside the range, the message “Number outside the range” was printed;
            - returned a list of numbers falling within the specified range.
'''

def test_range(start, end, *args):
    nums_in_range = []

    for cur_num in args:
        if cur_num in range(start, end+1):
            nums_in_range.append(cur_num)
        else:
            print('Number outside the range')

    return nums_in_range

start = 4
end = 12

print(test_range(start, end, 5, 16, 32, 6, 7, 1))