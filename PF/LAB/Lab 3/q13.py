# Q13 - Flight Ticket Cost Calculator

print("Flight Ticket Cost Calculator\n")

ticket = float(input("Ticket price: Rs."))
baggage = float(input("Baggage Price: Rs."))
air_tax = float(input("Airport Tax: Rs."))
hotel = float(input("Hotel Booking Charge: Rs."))

total = ticket + baggage + air_tax + hotel

print("Total Travel Cost >>> Rs." + str(total))