from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


# Draw out a sample for chi squared distribution with degree of freedom 2 with size 2x3:
x = random.chisquare(df=2, size=(2, 3))

print(x)


# Visualization of Chi Square Distribution
sns.distplot(random.chisquare(df=1, size=1000), hist=False)

plt.show()