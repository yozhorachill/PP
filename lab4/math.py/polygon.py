import math
def area_polygon(n,s):
    area= (n * s**2)/(4*math.tan(math.pi/n))
    return area
n= float(input("Number of sides:"))
s=float(input("Length of one side:"))
area=area_polygon(n,s)
print("Area of Polygon is",area)