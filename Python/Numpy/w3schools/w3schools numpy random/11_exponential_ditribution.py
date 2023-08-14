from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# Draw out a sample for exponential distribution with 2.0 scale with 2x3 size:
x = random.exponential(scale=2, size=(2, 3))

print(x)


# Visualization of Exponential Distribution
sns.distplot(random.exponential(size=1000), hist=False)

plt.show()