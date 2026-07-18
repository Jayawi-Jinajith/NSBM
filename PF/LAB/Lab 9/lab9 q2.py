# caculate total of 5 numbers entered by user

total = 0
i = 1

while i <= 5:
    num = int(input("Enter a Number: "))
    total += num
    i += 1
print(f"Total = {total}")
