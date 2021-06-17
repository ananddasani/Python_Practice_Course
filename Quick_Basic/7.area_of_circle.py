# program to take radius of circle form the user and calculate are of circle

import math

radius = float(input("enter the radius of circle to get area :: "))
area = math.pi * (radius ** 2)
print("Area of circle having radius : ", radius, " is :: ", round(area, 4))
