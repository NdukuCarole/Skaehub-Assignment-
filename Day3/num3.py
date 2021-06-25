import numpy as np
#array
x = input("Enter the the array ")

arr = np.array([x])
print("Original array:")
print(arr)
# size of array
print("Size of the memory occupied by the said array:")
print("%d bytes" % (arr.size * arr.itemsize))
