# Q9 - Cinema Ticket Booking System


print("Cinema Ticket Booking Calculator\n")

price_adultT = float(input("Enter the price of a adult ticket: Rs."))
price_childT = float(input("Enter the price of a child ticket: Rs."))
num_adultT = int(input("Enter the number of adult tickets: "))
num_childT = int(input("Enter the number of child tickets: "))
snack = float(input("Enter snack package cost: Rs."))

adultT = num_adultT * price_adultT
childT = num_childT * price_childT
total = adultT + childT + snack

print("-----Bill------")
print("Adult Tickets >>> " + str(num_adultT) + " x Rs." + str(price_adultT) + " = Rs." + str(adultT))
print("Child Tickets >>> " + str(num_childT) + " x Rs." + str(price_childT) + " = Rs." + str(childT))
print("Snack Package Cost = Rs." + str(snack))
print("\n Total Cost = Rs. " + str(total))