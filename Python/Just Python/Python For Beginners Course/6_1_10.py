""" 
Task: We call a number interesting if the difference between the maximum 
and minimum digits in it is equal to the average digit. 
Write a program that determines if a number is interesting or not. 
If the number is interesting, you should print "Number interesting", 
otherwise - "Number uninteresting".
"""
given_number = int(input())

digit_1 = given_number // 100
digit_2 = (given_number // 10) % 10
digit_3 = given_number % 10

max_digit = max(digit_1, digit_2, digit_3)
min_digit = min(digit_1, digit_2, digit_3)
sum_of_digits = digit_1 + digit_2 + digit_3

average_digit = sum_of_digits - max_digit - min_digit
diff_max_min = max_digit - min_digit

if diff_max_min == average_digit:
    print('Number interesting')
else:
    print('Number uninteresting')