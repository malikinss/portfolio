""" 
Task: The football team recruits girls from 10 to 15 years old inclusive. 
Write a program that queries the age and gender of an applicant using the gender designation letters m (from male - male) and f (from female - female) and determines whether the applicant is suitable for joining the team or not. 
If the applicant is suitable, then print "YES", otherwise print "NO".
"""
age = int(input())
sex = input()
if sex == 'f' and 10 <= age <= 15:
    print('YES')
else:
    print('NO')