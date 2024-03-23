'''
TODO: The Chinese horoscope assigns years to animals in a 12-year cycle. One 12 year cycle is shown in the table below.
Thus, 2012 will be another year of the dragon.
Write a program that reads the year and displays the name of the animal associated with it.
'''

year = int(input())

animals = ['Monkey', 'Rooster', 'Dog', 'Pig', 'Rat', 'Bull', 'Tiger', 'Hare', 'Dragon', 'Snake', 'Horse', 'Sheep']

print(animals[year % 12])