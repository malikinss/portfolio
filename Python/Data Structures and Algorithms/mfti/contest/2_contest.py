x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

def is_queen_can_go_there(start_x, start_y, end_x, end_y):
    if start_x == end_x or start_y == end_y:
        print("YES")
    elif start_x + start_y == end_x + end_y or start_x - start_y == end_x - end_y:
        print("YES")
    else:
        print("NO")

is_queen_can_go_there(x1, y1, x2, y2)        