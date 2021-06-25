import numpy as np
#array
x = input("Enter the the array ")

if len(x) >5:

    print("Enter more arrays")

else:

    arr = np.array([x])
    print("Original array:")
    print(arr)
    # size of array
    print("Size of the memory occupied by the said array:")
    print("%d bytes" % (arr.size * arr.itemsize))
