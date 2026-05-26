import math

#Q2 - calculate the area and circumference of a circle

r = float(input("Enter the radius of the circlr: "))
c = 2 * math.pi * r
a = math.pi * r ** 2
print("Circumference: " + str(c))
print("Area         : " + str(a))