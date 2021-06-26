import math


# nairobi co-ordinates
p1 = [1.2921, 36.8219]

#Cairo co-ordinates
p2 = [30.0444, 31.2357]

#computation of distance
distance = math.sqrt( ((int(p1[0])-int(p2[0]))**2)+((int(p1[1])-int(p2[1]))**2) )

#Output
print("distance between in Km",distance) 