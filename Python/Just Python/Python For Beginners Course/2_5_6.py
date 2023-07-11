""" 
Task: Write a program to convert a time interval given in minutes to a value expressed in hours and minutes.
"""
time = int(input())
hours = time // 60
mins = time % 60
print(time, 'mins this is:', hours, 'hours', mins, 'mins.')