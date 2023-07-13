""" 
Task: Two old women walk towards each other with constant speeds v1 and v2 km/h. Determine after what time (in hours) the old women will meet if the distance between them is S km.
"""
S = float(input())
v1 = float(input())
v2 = float(input())

t = S / (v1 + v2)

print(t)