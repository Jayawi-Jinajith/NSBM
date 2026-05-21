#Q1
print("Name: Jayawi Jinajith")
print("School: Hanwella Rajasinghe Central College")

# This is a standalone single-line comment
print("\ncomments")  # This is an inline comment

# This is line one of the comment
# This is line two of the comment
# This is line three of the comment

"""
This is a multi-line string used 
as a comment block. Python ignores it 
if it isn't assigned to a variable.
"""

# why use comments - explain code logic to humans,
#                    making software easier to understand, debug, and maintain.
print("")

#Q2
print("22 divided by 7 is:", 22/7)

result = 22/7
print("22 divided by 7 is:", result)
print("")

#Q3
# concatenation - 
operation = "Sum"
total = 8
print(operation, "is " + str(total))
print("")

#Q4
length = 10
width = 5
area = length * width
print("The area of a rectangle with length "
      + str(length)
      + " and width "
      + str(width)
      + " is "
      + str(area))
print("")

#Q5
name = input("Enter your name: ")
print("Hello " + name + ", welcome to NSBM")
print(type(name))
print("")

#Q6
birthYear = input("Enter your birth year: ")
birthYear = int(birthYear)
print("Your birth year is "
      + str(birthYear))

# Typecasting - changing data type to another
print(type(birthYear))
print("")

#Q7
birthYear = int(input("Enter your birth year: "))
currentYear = 2025
age = currentYear - birthYear
print("Your age is: "
      + str(age))
print("")

#Q8-bonus
num1 = input("Enter number 1: ")
num2 = input("Enter number 2: ")
num1 = int(num1)
num2 = int(num2)
add = num1 + num2
sub = num1 - num2
multiply = num1 * num2
div = num1 / num2
power = num1 ** num2
print(  "\n addition       >>> " + str(add)
      + "\n substraction   >>> " + str(sub)
      + "\n multiplication >>> " + str(multiply)
      + "\n division       >>> " + str(div)
      + "\n power          >>> " + str(power))

