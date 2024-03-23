'''
TODO: Pascal's triangle is an infinite table of binomial coefficients that has a triangular shape. In this triangle, there are ones at the top and on the sides. Each number is equal to the sum of the two numbers above it.

The number n is given as input to the program.
Write a program that returns the specified string of Pascal's triangle as a list (line numbering starts from zero).

NOTE: The solution can be conveniently expressed as the pascal() function, which takes a line number and returns the corresponding line of Pascal's triangle.
'''

def pascal(n):
    # start line
    cur_seq = [1]

    for _ in range(n):
        # add zeros to the sides of the current line
        cur_seq = [0] + cur_seq + [0]
        # newline will be stored here
        new_seq = []

        for i in range(len(cur_seq) - 1):
            # add to the new line the sum of adjacent elements of the current line
            new_seq.append(cur_seq[i] + cur_seq[i + 1])

        # now the new line becomes our current line
        cur_seq = new_seq

    return cur_seq


n = int(input())
print(pascal(n))
    