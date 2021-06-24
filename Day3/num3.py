import numpy as np

#array
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print("Original array:")
print(arr)
# size of array
print("Size of the memory occupied by the said array:")
print("%d bytes" % (arr.size * arr.itemsize))