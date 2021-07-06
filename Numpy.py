import numpy as np
from matplotlib import  pyplot as plt

ar = np.array([1, 2, 3])
print(np.exp(ar))
print(np.log(ar))
print(np.log10(ar))







x = np.arange(0, 3*np.pi, 0.1)
y = np.tan(x)

plt.plot(x, y)
plt.show()




a = np.array([(1, 2, 3, 4, 5, 6, 7), (8, 9, 10, 11, 12, 13, 14)])
print(a.ndim)
print(a.itemsize)
print(a.size)
print(a.shape)

print('=============================================')

a = np.array([(1, 2, 3, 4), (3, 4, 5, 6), (7, 8, 9, 10)])
# print(a)
# a = a.reshape(4, 2)
print(a)

# Slicing
print(a[0:2, 3]) # Slicing when dealing with numpy arrays
print('\n')
a = np.linspace(1, 3, 5)
print(a)
print('\n')
a = np.array([1, 2, 3])
print(a.min())
print(a.max())
print(a.sum())
a = [2, 3, 1, 3]
import math
print(math.fsum(a))

# Axis concept
a = np.array([(1, 2, 3), (2, 4, 5)])
print(a.sum(axis= 1))

print('\n')
print(np.sqrt(a))
print(np.std(a))

print('\n')
a = np.array([(1, 2, 3), (3, 4, 5)])
b = np.array([(1, 2, 3), (3, 4, 5)])

print(a / b)

print(np.vstack((a, b)))
print(np.hstack((a, b)))

print(a.ravel())

