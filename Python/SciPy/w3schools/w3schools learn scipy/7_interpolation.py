from scipy.interpolate import interp1d
from scipy.interpolate import UnivariateSpline
from scipy.interpolate import Rbf
import numpy as np


# For given xs and ys interpolate values from 2.1, 2.2... to 2.9:
xs = np.arange(10)
ys = 2*xs + 1

interp_func = interp1d(xs, ys)

newarr = interp_func(np.arange(2.1, 3, 0.1))

print(newarr)


# Find univariate spline interpolation for 2.1, 2.2... 2.9 for the following non linear points:
xs = np.arange(10)
ys = xs**2 + np.sin(xs) + 1

interp_func = UnivariateSpline(xs, ys)

newarr = interp_func(np.arange(2.1, 3, 0.1))

print(newarr)


# Interpolate following xs and ys using rbf and find values for 2.1, 2.2 ... 2.9:
xs = np.arange(10)
ys = xs**2 + np.sin(xs) + 1

interp_func = Rbf(xs, ys)

newarr = interp_func(np.arange(2.1, 3, 0.1))

print(newarr)