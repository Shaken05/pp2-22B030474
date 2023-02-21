#1
import math
degree=int(input("Input degree: "))
radian=math.radians(degree)
print("Output radian:",radian)


#2
height=int(input("Height: "))
first_value=int(input("Base, first value: "))
second_value=int(input("Base, second value: "))
area_trapezoid=0.5*(first_value+second_value)*height
print("Area of a trapezoid:",area_trapezoid)

#3
sides=int(input("Input number of sides: "))
length=int(input("Input the length of a side: "))
perimeter=sides*length
apothem=length / (2*math.tan(math.pi/sides))
area=int((perimeter*apothem) / 2)
print("The area of the polygon is:", area)

#4
base_length = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))
area = base_length * height
print("Area of parallelogram:", area)
