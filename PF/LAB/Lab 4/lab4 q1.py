# Q1 - Swap values of 2 numbers

# 1st way
print("Path 1\n")

a = int(input("Number 1 (a): "))
b = int(input("number 2 (b): "))

print("Before 'a' is " + str(a))
print("Before 'b' is " + str(b))

c = a
a = b
b = c

print("After 'a' is " + str(a))
print("After 'b' is " + str(b))

# 2nd way
print("\nPath 2\n")

x = int(input("Number 1 (x): "))
y = int(input("number 2 (x): "))

x = x + y
y = x - y
x = x - y

print("x >>> " + str(x))
print("y >>> " + str(y))
