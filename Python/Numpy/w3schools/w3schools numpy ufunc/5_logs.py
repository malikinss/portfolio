import numpy as np


# Find log at base 2 of all elements of following array:
arr = np.arange(1, 10)

print(np.log2(arr))


# Find log at base 10 of all elements of following array:
arr = np.arange(1, 10)

print(np.log10(arr))


# Find log at base e of all elements of following array:
arr = np.arange(1, 10)

print(np.log(arr))


# Log at Any Base
from math import log

nplog = np.frompyfunc(log, 2, 1)

print(nplog(100, 15))