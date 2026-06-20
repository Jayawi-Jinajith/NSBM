# Finding the maximum sale 

sale = float(input("Sale: "))
max = sale
i = 2

while i <= 10:
    sale = float(input("Sale: "))
    if sale > max:
        max = sale
    i = i + 1

print("Maximum Sale is ", max)