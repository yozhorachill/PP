import math
def area_trapezoid(b1,b2,h):
    area=(b1+b2)/2 * h
    return area
b1=float(input("base 1:"))
b2=float(input("base 2:"))
h=float(input("height:"))
 
area=area_trapezoid(b1,b2,h)
print("Expected output:",area)