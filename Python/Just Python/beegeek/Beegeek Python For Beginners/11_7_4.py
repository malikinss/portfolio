'''
Complete the above code using a list expression so that you get a list of all palindrome numbers from 100 to 1000.
Note. The resulting list must consist of integers.
'''

palindromes = [i for i in range(100, 1001) if str(i) == str(i)[::-1]]

print(palindromes)