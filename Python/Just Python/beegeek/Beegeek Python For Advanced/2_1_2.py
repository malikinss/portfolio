'''
TODO: Write a program to calculate and estimate a person's body mass index (BMI). BMI shows whether a person weighs more or less than normal for his height. A person's BMI is calculated using the formula:

BMI = mass / height^2

where mass is measured in kilograms and height in meters.

A person's weight is considered optimal if his BMI is between 18.5 and 25.

If the BMI is less than 18.5, then the person is considered to be underweight.
If the BMI value is more than 25, then the person is considered to be overweight.

The program should output:
"Optimal weight" if the BMI is between 18.5 and 25 (inclusive).
"Underweight" if BMI is less than 18.5.
"Overweight" if the BMI value is greater than 25.
'''

weight, height = float(input()), float(input())
bmi = weight / height ** 2

if bmi > 25:
    print('Optimal weight')
elif bmi < 18.5:
    print('Underweight')
else:
    print('Overweight')
