# Q1 - Hotel Billing System

roomCharge = float(input("Enter the room charges per day: Rs."))
days = int(input("Enter the number of days: "))
foodCharge = float(input("Enter the food charges: Rs."))
servPercent = float(input("Enter the service charge percentage(%): "))

subtotal = roomCharge * days + foodCharge
servCharge = subtotal * servPercent * 0.01
finalBill = subtotal + servCharge

print("SubTotal: " + str(subtotal)
      + " |  Service Charge: " + str(servCharge)
      + " |  Final Bill: " + str(finalBill))