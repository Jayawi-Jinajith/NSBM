# Q3 - Gocery Store

i = 0
total = 0

while True:
    price = float(input(f"Price - Item {i + 1}: "))
    if price == 0:
        break
    total += price
    i += 1
    
if i > 0:
    avg = total / i
else:
    avg = 0
print(f"Total Bill = Rs.{total}")
print(f"Items Count = {i}")
print(f"Average Price = Rs.{avg}")
