'''
TODO:   
        Implement the index_of_nearest() function, which takes two arguments in the following order:

            numbers — a list of integers
            number — an integer

        The function must find the number closest to the number in the numbers list and return its index. 

        If the numbers list is empty, the function should return the number -1.

NOTE:   
        If a list containing several numbers that are simultaneously closest to the desired number is passed to the function, the function must return the smallest of the indexes of the nearest numbers.
'''

def get_diffirences(numbers, number):
    diff_list = []

    for cur_number in numbers:
        difference = cur_number - number
        
        if difference < 0:
            difference *= -1

        diff_list.append(difference)

    return diff_list

def index_of_nearest(numbers, number):
    if 0 == len(numbers):
        return -1
     
    diff_list = get_diffirences(numbers, number)
    min_diffirence = min(diff_list)
    result_index = diff_list.index(min_diffirence)

    return result_index

def id_of_nearest(nums, n):
    if nums:
        minimum = min(nums, key=lambda num: abs(num - n))
        return nums.index(minimum)
    return -1