import numpy as np
from scipy.stats import ttest_ind
from scipy.stats import kstest
from scipy.stats import describe
from scipy.stats import skew, kurtosis
from scipy.stats import normaltest


# Find if the given values v1 and v2 are from same distribution:
v1 = np.random.normal(size=100)
v2 = np.random.normal(size=100)

res = ttest_ind(v1, v2)

print(res)


# Find if the given value follows the normal distribution:
v = np.random.normal(size=100)

res = kstest(v, 'norm')

print(res)


# Show statistical description of the values in an array:
v = np.random.normal(size=100)
res = describe(v)

print(res)


# Find skewness and kurtosis of values in an array:
v = np.random.normal(size=100)

print(skew(v))
print(kurtosis(v))


# Find if the data comes from a normal distribution:
v = np.random.normal(size=100)

print(normaltest(v))