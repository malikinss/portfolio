import matplotlib.pyplot as plt
import numpy as np


# A simple histogram:
x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show()