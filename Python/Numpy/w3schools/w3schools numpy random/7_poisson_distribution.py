from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


# Generate a random 1x10 distribution for occurrence 2:
x = random.poisson(lam=2, size=10)

print(x)


# Visualization of Poisson Distribution
sns.distplot(random.poisson(lam=2, size=1000), kde=False)

plt.show()


# Difference Between Normal and Poisson Distribution
sns.distplot(random.normal(loc=50, scale=7, size=1000), hist=False, label='normal')
sns.distplot(random.poisson(lam=50, size=1000), hist=False, label='poisson')

plt.show()


# Difference Between Binomial and Poisson Distribution
sns.distplot(random.binomial(n=1000, p=0.01, size=1000), hist=False, label='binomial')
sns.distplot(random.poisson(lam=10, size=1000), hist=False, label='poisson')

plt.show()