import math

#user input
d = int(input("Enter your number "))


#calculation and condition verificatin
root = math.sqrt(d)

#Output expected in case of failure or success
if int(root + 0.5) ** 2 == d:
    print(d, "is a perfect square")
else:
    print(d, "is not a perfect square")