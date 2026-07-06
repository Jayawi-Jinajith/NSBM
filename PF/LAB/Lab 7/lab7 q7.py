# Q7 - Product Sales Report

highest = 0
total = 0

for day in range(7):
    sale = float(input(f"Sale Amount - Day {day+1}: "))
    if sale > highest:
        highest = sale
    if day == 0:
        lowest = sale
    if sale < lowest:
        lowest = sale
    total += sale

avg = total / (day+1)
print(f"Total weekly sales = Rs.{total}")
print(f"Average daily sales = Rs.{avg}")
print(f"Highest sale = Rs.{highest}")
print(f"Lowest sale = Rs.{lowest}")

        
