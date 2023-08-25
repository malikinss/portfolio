'''
TODO: Write a draw_triangle() function that draws a star right triangle with legs equal to 10
'''

def draw_triangle():
    print(*['*' * i for i in range(1, 11)], sep='\n')


draw_triangle()