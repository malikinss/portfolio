from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


# Create a 2x3 uniform distribution sample:
x = random.uniform(size=(2, 3))

print(x)


# Visualization of Uniform Distribution
sns.distplot(random.uniform(size=1000), hist=False)

plt.show()