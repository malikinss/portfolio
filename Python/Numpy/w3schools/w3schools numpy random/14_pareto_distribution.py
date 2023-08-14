from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


# Draw out a sample for pareto distribution with shape of 2 with size 2x3:
x = random.pareto(a=2, size=(2, 3))

print(x)


# Visualization of Pareto Distribution
sns.distplot(random.pareto(a=2, size=1000), kde=False)

plt.show()