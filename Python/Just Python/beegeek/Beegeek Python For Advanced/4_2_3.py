'''
TODO: The trace of a square matrix is the sum of the elements of the main diagonal. 
Write a program that prints the trace of a given square matrix.
'''

n = int(input())
sm = 0

for i in range(n):
    cur_seq = input().split()
    sm += int(cur_seq[i])

print(sm)