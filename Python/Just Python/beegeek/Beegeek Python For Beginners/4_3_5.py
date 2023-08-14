""" 
Task: Known weight of an amateur boxer (integer). 
It is known that the weight is such that a boxer can be 
assigned to one of three weight categories:
Light weight - up to 60 kg;
First welterweight - up to 64 kg;
Welterweight - up to 69 kg.
Write a program that determines which category a given boxer will compete in.
"""
weight = int(input())
if weight < 60:
    print('Light weight')
elif weight < 64:
    print('First welterweight')
else:
    print('Welterweight')