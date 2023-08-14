import numpy
from scipy import stats


# Use the NumPy mean() method to find the average speed:
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.mean(speed)

print(x)


# Use the NumPy median() method to find the middle value:
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.median(speed)

print(x)


# If there are two numbers in the middle, divide the sum of those numbers by two.
speed = [99,86,87,88,86,103,87,94,78,77,85,86]

x = numpy.median(speed)

print(x)


# Use the SciPy mode() method to find the number that appears the most:
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = stats.mode(speed)

print(x)