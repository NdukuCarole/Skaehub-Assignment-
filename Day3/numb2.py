import numpy as np

# userinput
x = input("Enter the start date in the format: Year-Month ")
y = input("Enter the End date date in the format: Year-Month ")

# weekend computation
ans = np.busday_count(x , y)
  
  #Output
print(ans)
