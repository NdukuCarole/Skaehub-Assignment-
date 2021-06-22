#defining the function for leap 
def is_leap(year):
    leap = False
    
    # checking whether the input meets the conditions
    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True
    
    return leap
    
    #user Input data
year = int(input())

# output after conditions are checked
print (is_leap(year))