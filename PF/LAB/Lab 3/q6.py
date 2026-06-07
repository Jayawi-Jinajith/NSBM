# Q6 - Gym Membership Payment Systems

month_fee = float(input("Enter the Gym Membership monthly fee: Rs."))
months = int(input("Enter the number of months: "))
reg_fee = float(input("Enter the Registration fee: Rs."))
trainer_fee = float(input("Enter the Personal Trainer's fee: Rs."))
tax_percent = float(input("Enter the tax percentage (%): "))

total = (month_fee * months) + reg_fee + trainer_fee
tax = total * tax_percent / 100
final = total + tax

print("\nTotal fee(without tax) >>>" + str(total))
print("                   Tax >>>" + str(tax))
print("   Final fee(with tax) >>>" + str(final))