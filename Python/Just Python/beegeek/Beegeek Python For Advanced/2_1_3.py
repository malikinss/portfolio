'''
TODO: Given a line of text.
Write a program to calculate the cost of a string, based on the fact that any one character (including a space) costs 50 cents.
Give your answer in dollars and cents according to the examples.
'''

input_string = input()

each_char_price = 50
length_of_string = len(input_string)

string_total_price_in_cents = length_of_string * each_char_price

dollars = string_total_price_in_cents // 100
cents = string_total_price_in_cents % 100

print(dollars, 'dollars', cents, 'cents')
