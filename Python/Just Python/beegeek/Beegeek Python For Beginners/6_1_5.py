""" 
Task: The input to the program is the number n - the number of dog years. 
Write a program that calculates the age of a dog in human years.
For the first two years, a dog year is 10.5 human years. 
After that, each year of the dog is equal to 4 human years.
"""
dog_years = float(input())

if dog_years <= 2:
    human_years = dog_years*10.5
else:
    human_years = 21+(dog_years-2)*4

print(human_years)