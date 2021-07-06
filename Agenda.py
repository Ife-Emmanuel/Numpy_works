"""creating numpy array"""
import Numpy as np
import time
import sys

# a = np.array([[2, 3, 5], [2, 1, 0]])
# print(a)
size = 1000
a = range(size)
print(sys.getsizeof(5) * len(a))
A = np.arange(size)
print(A.size * A.itemsize)
B = np.arange(size)

#print(sys.getsizeof(5) * size)


# size = 1000000
#
# l1 = range(size)
# l2 = range(size)
#
# a1 = np.arange(size)
# a2 = np.arange(size)
#
# start = time.time()
#
# result = [(x  +  y) for x, y in zip(l1, l2)]
# print((time.time() - start) * 1000)
# #print('\nresult', result)
#
# start = time.time()
# result  = a1 + a2
#
# print((time.time() - start) * 1000)
#print('\nresult', result)











# s = range(1000)
# print(sys.getsizeof(5) * len(s))
#
# d = np.arange(1000)
# print(d.size * d.itemsize)
# # print(sys.getsizeof(5) * len(d))