# Q5 - Sum of numbers

# accept numbers till user enter "-1"

sum = 0

while True:
    num = int(input("Enter a Number: "))
    if num == -1:
        break
    sum = sum + num
    
print("Sum >>> ", sum)
