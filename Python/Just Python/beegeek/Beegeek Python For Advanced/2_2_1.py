'''
TODO: Given a set of points on a coordinate plane. 
Count and print the number of points lying in each coordinate quadrant.
The first line contains the number of points. 
Each next line consists of two integers - the coordinates of the point (first the abscissa - x, then the ordinate - y), separated by a space character.
NOTE: Please note that points lying on the coordinate axes are not usually assigned to any coordinate quadrant.
'''

n = int(input())
count = [0, 0, 0, 0]
names = ['First quarter:', 'Second quarter:', 
         'Third quarter:', 'Fourth quarter:']

for _ in range(n):
    x, y = [int(num) for num in input().split()]

    if x > 0 and y > 0:
        count[0] += 1
    
    elif x < 0 and y > 0:
        count[1] += 1
    
    elif x < 0 and y < 0:
        count[2] += 1
    
    elif x > 0 and y < 0:
        count[3] += 1
        
for i in range(4):
    print(names[i], count[i])