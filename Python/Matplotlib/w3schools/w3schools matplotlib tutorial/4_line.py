import matplotlib.pyplot as plt
import numpy as np

# Use a dotted line:
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, linestyle = 'dotted')
plt.show()

# Shorter syntax:
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, ls = ':')
plt.show()

# Use a dashed line:
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, linestyle = 'dashed')
plt.show()

# Set the line color to red:
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, color = 'r')
plt.show()

# Plot with a beautiful green line:
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, c = '#4CAF50')
plt.show()

# Plot with the color named "hotpink":
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, c = 'hotpink')
plt.show()

# Plot with a 20.5pt wide line:
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, linewidth = '20.5')
plt.show()

# Draw two lines by specifying a plt.plot() function for each line:
y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])
plt.plot(y1)
plt.plot(y2)
plt.show()

# Draw two lines by specifiyng the x- and y-point values for both lines:
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])
plt.plot(x1, y1, x2, y2)
plt.show()