'''
TODO: The program input is a natural number n.
Write a program that prints the first n lines of Pascal's triangle.

NOTE: The solution can be conveniently expressed as the pascal() function, which takes a line number and returns the corresponding line of Pascal's triangle.
'''

def pascal(n):
    # result table
    seq = [[1]]
    # starting line
    cur_seq = [1]

    for _ in range(n - 1):
        # add zeros to the sides of the current line
        cur_seq = [0] + cur_seq + [0]
        # newline will be stored here
        new_seq = []

        for i in range(len(cur_seq) - 1):
            # add to the new line the sum of adjacent elements of the current line
            new_seq.append(cur_seq[i] + cur_seq[i + 1])

        # now the new line becomes our current line
        cur_seq = new_seq
        # add the current row to the resulting table
        seq.append(cur_seq)

    return seq


n = int(input())
seq = pascal(n)

# display the table row by row
for s in seq:
    print(*s)
    