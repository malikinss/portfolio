""" 
Task: Complete the following code using string formatting with the 
format method so that it outputs text:

"In 2010, someone paid 10k Bitcoin for two pizzas." (without quotes).
"""

# original code
s = 'In {0}, someone paid {1} {2} for two pizzas.'
print()

# fixed code
year = 2010
price = '10k'
value = 'Bitcoin'

s = 'In {0}, someone paid {1} {2} for two pizzas.'.format(year, price, value)

print(s)