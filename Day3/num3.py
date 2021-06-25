# import library
import numpy as np
# create list
y = []
# ask the size of array needed
x = int(input("Size of array:\n"))
# ask user to input the element they want to put
for i in range(x):
    #add data to the list
    y.append(float(input("Element:\n")))
# change the list to a numpy array
y = np.array(y)
print(y)
# check the length of array
if len(y) >5:
    # get the size of the array
    print("Size of the array: ",
          y.size)
    # get the memory size of one array element
    print("Memory size of one array element in bytes: ",
          y.itemsize)
    # memory size of numpy array in bytes(all elements)
    print("Memory size of numpy array in bytes:",
          y.size * y.itemsize)
