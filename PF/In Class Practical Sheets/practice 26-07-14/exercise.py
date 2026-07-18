num = int(input("Positive Integer Number: "))

while True:
    if num == 1:
        break
    if num % 2 == 0:
        num /= 2
    else:
        num = (num*3) + 1
    print(f"{num:.0f}")