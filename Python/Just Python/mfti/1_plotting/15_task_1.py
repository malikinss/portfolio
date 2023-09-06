import numpy as np
import matplotlib.pyplot as plt


x = [1, 10, 1000]


dividend = (1 / (np.exp(np.sin(x) + 1)))
    
divisor = (1.25 + (1 / np.power(x, 15)))

quotient = (dividend / divisor)

y = np.log(quotient) / np.log(1 + np.power(x, 2))

'''    
print("**************")
print(dividend)
print(divisor)
print(quotient)

print(y)
print()
'''

plt.plot(x, y)
plt.show()