import matplotlib.pyplot as plt
import numpy as np

# Mark each point with a circle:
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o')
plt.show()

# Mark each point with a star:
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = '*')
plt.show()

# Mark each point with a circle with fmt parameters:
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, 'o:r')
plt.show()

# Set the size of the markers to 20:
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o', ms = 20)
plt.show()

# Set the EDGE color to red:
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
plt.show()

# Set the FACE color to red:
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')
plt.show()

# Set the color of both the edge to green and the face to red:
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'g', mfc = 'r')
plt.show()

# Mark each point with a beautiful green color:
plt.plot(ypoints, marker = 'o', ms = 20, mec = '#4CAF50', mfc = '#4CAF50')

# Mark each point with the color named "hotpink":
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'hotpink', mfc = 'hotpink')