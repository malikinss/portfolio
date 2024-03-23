'''
TODO:
        The get_mean() function receives a list of numbers as input.

        Write the function code so that it returns the arithmetic mean of the numbers from the resulting list.

        Call the get_mean() function with the argument num_lst; print the result of the call, rounded to two decimal places.
'''

def get_mean(values):
    result = round(sum(values) / len(values),2)
    return result

num_lst = [3, 6, 5, 7, 9, 1]
print(get_mean(num_lst))
