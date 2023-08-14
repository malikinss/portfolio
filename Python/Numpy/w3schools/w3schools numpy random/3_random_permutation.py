from numpy import random
import numpy as np

# Randomly shuffle elements of following array:
arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)
print(arr)

# Generate a random permutation of elements of following array:
arr = np.array([1, 2, 3, 4, 5])
new_arr = random.permutation(arr)
print(new_arr)