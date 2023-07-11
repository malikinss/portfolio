""" 
Task: Write a program that takes a number as input and outputs the text "YES" or "NO" depending on the conditions.
Conditions:
if the number is odd, then output "YES";
if the number is even in the range from 2 to 5 (inclusive), then output "NO";
if the number is even in the range from 6 to 20 (inclusive), then output "YES";
if the number is even and greater than 20, then output "NO".
"""
number = int(input())
odd_or_even = number % 2
if odd_or_even != 0:
    print('YES')
elif odd_or_even == 0 and 2 <= number <= 5:
    print('NO')
elif odd_or_even == 0 and 6 <= number <= 20:
    print('YES')
elif odd_or_even == 0 and 20 <= number:
    print('NO')