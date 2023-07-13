""" 
Task: The famous American writer Ray Bradbury has a novel Fahrenheit 451. 
Write a program that determines what temperature on the Celsius scale 
corresponds to the specified value on the Fahrenheit scale.
Use the formula to translate: C = (5 / 9) * (F - 32)
"""
fahrenheit = float(input())

celsium = (5/9)*(fahrenheit-32)

print(celsium)