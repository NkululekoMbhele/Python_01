
#A program that gives basic vector calculations in 3 dimensional
#Nkululeko Mbhele
#06 April 2019

import math

print("Enter vector A: ")
a, b, c = [int(x) for x in input().split()]
print("Enter vector B: ")
x, y, z = [int(x) for x in input().split()]


# addition

add = [a+x,b+y,c+z]
print("A+B =",add)

#dot product
dot = a*x+b*y+c*z
print("A.B =",dot)

da = a**2 + b**2 + c**2
da = math.sqrt(da)
print("|A| =",'{:.2f}'.format(round(da,2)))

db = x**2 + y**2 + z**2
db = math.sqrt(db)
print("|B| =",'{:.2f}'.format(round(db,2)))