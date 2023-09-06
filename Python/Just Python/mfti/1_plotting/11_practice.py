import numpy as np
import matplotlib.pyplot as plt


# evenly distributed values from 0 to 5, in increments of 0.2
t = np.arange(0., 5., 0.2)

# red lines, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')

plt.show()