from scipy import io
import numpy as np


# Export the following array as variable name "vec" to a mat file:
arr = np.arange(10)

io.savemat('arr.mat', {"vec": arr})


# Import the array from following mat file.:
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,])

io.savemat('arr.mat', {"vec": arr}) # Export
mydata = io.loadmat('arr.mat') # Import

print(mydata)