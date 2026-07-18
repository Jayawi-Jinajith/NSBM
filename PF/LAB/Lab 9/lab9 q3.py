# find odd or even numbers

even = 0
odd = 0
i = 1
while i <= 5:
    num = int(input("Number: "))
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
    i += 1

print(f"Even x {even}")
print(f"Odd  x {odd}")
