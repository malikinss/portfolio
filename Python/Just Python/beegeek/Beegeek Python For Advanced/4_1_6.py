'''
TODO: The program receives two lines as input: one contains symbols, the other contains the number n. A list is formed from the first line.

Implement the chunked() function, which takes as input a list and a number specifying the chunk size, and returns a list of chunks of the specified length.
'''

def chunked(symbols, n):
    result = []
    for i in range(0, len(symbols), n):
        result.append(symbols[i:i + n])
    return result

symbols = input().split()
n = int(input())

print(chunked(symbols, n))