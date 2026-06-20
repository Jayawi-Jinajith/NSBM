# Q7 - calculate factorial value of given number

print("Enter the number which you want to calculate factorial of it")
number = int(input("Number: "))
num = number
fact = 1

while num > 0:
    fact = fact * num
    if num == 1:
        print(str(num))
    else:
        print(str(num), "x", end=" ")
    num = num - 1
print(str(number), "! = ", str(fact))