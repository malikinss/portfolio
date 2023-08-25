'''
Write a draw_box() function that draws a 14x10 star box, as shown:

**********
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
**********
'''

def draw_box():
    for i in range(14):
        if i == 0 or i == 13:
            print('*' * 10)
        else:
            print('*' + ' ' * 8 + '*')

draw_box()