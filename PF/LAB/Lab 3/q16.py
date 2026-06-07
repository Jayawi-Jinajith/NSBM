# Q16 - Resturant Billing System

print("Resturant Billing System\n")

meal = float(input("Price of the Meal: "))
beverage = float(input("Price of the Beverage: "))
dessert = float(input("Price of the Dessert: "))
serv_charge_percenr = float(input("Service Charge Percentage (%): "))
tax_percent = float(input("Tax Percentage (%): "))

food = meal + beverage + dessert
serv_charge = food * serv_charge_percenr / 100
total_withoutTax = food + serv_charge
tax = total_withoutTax * tax_percent / 100
total = total_withoutTax + tax

print("          Food >>> " + str(food))
print("Service Charge >>> " + str(serv_charge))
print("           Tax >>> " + str(tax))
print("\n    Total Bill >>> " + str(total))