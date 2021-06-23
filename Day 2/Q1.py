def is_Power_of_four(n):

    #checking if conditions are met
    while n and not (n & 0b11):
        n >>= 2
    return (n == 1)

#user input
n = int(input("please enter positive integer "))

#Output
print(n, "   " ,is_Power_of_four(n))

