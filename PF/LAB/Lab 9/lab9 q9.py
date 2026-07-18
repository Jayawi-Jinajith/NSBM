# Multiplication table (3x5)

i = 1
while i <= 3:
    j = 1
    while j <= 5:
        print(f"{i*j:3}",end="")
        j += 1
    print()
    i += 1
