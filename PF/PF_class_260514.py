import math

#Q1 - calculate the average marks of 5 students

mark1 = int(input("Enter mark of student 1: "))
mark2 = int(input("Enter mark of student 2: "))
mark3 = int(input("Enter mark of student 3: "))
mark4 = int(input("Enter mark of student 4: "))
mark5 = int(input("Enter mark of student 5: "))
# can use float() or int() - type casting
total = mark1 + mark2 + mark3 + mark4 + mark5
avg = total / 5
print("Total: " + str(total)
      + "  | Average: " + str(avg))

#Q2 - calculate the area and circumference of a circle

r = float(input("Enter the radius of the circlr: "))
c = 2 * math.pi * r
a = math.pi * r ** 2
print("Circumference: " + str(c))
print("Area         : " + str(a))

#Q3 - calculate compound interest

p = float(input("Enter the principal amount: Rs."))
i = float(input("Enter the annual interest rate: %"))
t = int(input("Enter the number of years: "))

CI = p * (1 + (i / 100))**t - p
CI = round(CI, 2)
# round(value, decimal_places) - rounds a number to specificied number of decimals
#                              - not accurate: halfway .5 decimals somtimes will break
#                              - work behavio with float and int data types can be bit confusing
# f"(value:.2f)" - string formatted method (best)
print("Compound Interest is Rs." + str(CI))

#Q4 - calculate the final salary with allowance, extra work and tax deduction

bs = float(input("Enter the basic sallary: Rs."))
d = int(input("Enter the number of working days: "))
exH = int(input("Enter the extra hours worked: "))

fs = bs + d*bs*0.05 + exH*250 # fs - final salary
tax = fs * 0.12
fs = fs - tax
print("Salary: Rs." + str(fs))
