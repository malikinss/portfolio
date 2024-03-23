'''
TODO:   
        Let's call a set of different natural numbers a group. 
        For example: (13,4,22,40).
        Then the length of the group will be the number of numbers in the group. 
        For example, the length of the group (13,4,22,40) is 4.

        A sequence of natural numbers from 1 to n inclusive is given. 

        Write a program that groups all the numbers in a given sequence by the sum of their digits and determines the length of the group containing the largest number of numbers.

NOTE:   
        Consider the third test, in which n=20. 
        Let's write down a sequence of numbers from 1 to 20:
            1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20

        Let's group the obtained numbers by the sum of their digits:
            (1,10), (2,11,20), (3,12), (4,13), (5,14), (6,15), (7,16), (8,17), (9,18), (19)

        So, the length of the group with the largest number of numbers is 3.
'''

def calculate_digits_sum_in_number(number):
    """Calculates the sum of digits in a given number."""
    return sum(int(digit) for digit in str(number))

def get_sum_of_digits_in_number_groups(n):
    """Groups numbers based on the sum of their digits."""
    groups_dict = {}

    for i in range(1, n + 1):
        key = calculate_digits_sum_in_number(i)

        if key not in groups_dict:
            groups_dict[key] = [i]
        else:
            groups_dict[key].append(i)

    return groups_dict

def find_max_group_length(n):
    """Finds the length of the group with the largest number of numbers."""
    groups = get_sum_of_digits_in_number_groups(n)
    max_group_length = max(len(group) for group in groups.values())
    
    return max_group_length


print(find_max_group_length(int(input())))
