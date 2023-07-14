""" 
Task: Enhance the code below using f-string formatting so that it 
outputs the text:

"In 2010, someone paid 10K Bitcoin for two pizzas." (without quotes).
"""

# original code
year = 2010
amount = '10K'
currency = 'Bitcoin'

print('In {}, someone paid {} {} for two pizzas.')

# fixed code
year = 2010
amount = '10K'
currency = 'Bitcoin'

print(f'In {year}, someone paid {amount} {currency} for two pizzas.')