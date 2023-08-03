from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


# Draw out a sample for rayleigh distribution with scale of 2 with size 2x3:
x = random.rayleigh(scale=2, size=(2, 3))

print(x)


# Visualization of Rayleigh Distribution
sns.distplot(random.rayleigh(size=1000), hist=False)

plt.show()