import numpy as np


# Find sine value of PI/2:
x = np.sin(np.pi/2)

print(x)


# Find sine values for all of the values in arr:
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])

x = np.sin(arr)

print(x)


# Convert all of the values in following array arr to radians:
arr = np.array([90, 180, 270, 360])

x = np.deg2rad(arr)

print(x)


# Convert all of the values in following array arr to degrees:
arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])

x = np.rad2deg(arr)

print(x)


# Find the angle of 1.0:
x = np.arcsin(1.0)

print(x)


# Find the angle for all of the sine values in the array
arr = np.array([1, -1, 0.1])

x = np.arcsin(arr)

print(x)


# Find the hypotenues for 4 base and 3 perpendicular:
base = 3
perp = 4

x = np.hypot(base, perp)

print(x)