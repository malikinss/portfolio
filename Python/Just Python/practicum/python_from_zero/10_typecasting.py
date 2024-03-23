'''
TODO:
        Cast the variables to the desired type, perform the necessary operations on them, pass the values to the f-string and print the phrase:
            The sum of numbers 1, 2 and 3 is 6
'''

a = 1
b = '2'
c = ['Antony', 3.15, '3 piglets']

b = int(b)
c = int(c[2].split()[0])

print(f'The sum of numbers {a}, {b} and {c} is {a+b+c}')