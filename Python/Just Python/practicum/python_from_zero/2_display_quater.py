'''
TODO: 
        Write a program that, when run, gets the x and y values, the coordinates of a point on the plane. 
        The program must determine in which quarter on the coordinate plane the point with the transmitted coordinates is located.
'''

def display_quater(x, y):
    quaters = ['First Quater', 'Second Quater', 'Third Quater', 'Fourth Quater']
    
    positive_x = x > 0
    negative_x = x < 0

    positive_y = y > 0
    negative_y = y < 0

    if positive_x and positive_y:
        print(quaters[0])
    elif negative_x and positive_y:
        print(quaters[1])
    elif negative_x and negative_y:
        print(quaters[2])
    elif positive_x and negative_y:
        print(quaters[3])     
    else:
        print('Axis')

display_quater(1, 1)
display_quater(-1, -1)
display_quater(1, -1)
display_quater(-1, 1)
display_quater(0, 1)