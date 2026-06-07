# Q5 - Online Shopping Invoice

print("Product 1\n")
p1_name = input("Enter the name of the product: ")
p1_price = float(input("Enter the price of the product: "))
p1_quantity = int(input("Enter the quantity of the product: "))

print("\nProduct 2\n")
p2_name = input("Enter the name of the product: ")
p2_price = float(input("Enter the price of the product: "))
p2_quantity = int(input("Enter the quantity of the product: "))

print("\nProduct 3\n")
p3_name = input("Enter the name of the product: ")
p3_price = float(input("Enter the price of the product: "))
p3_quantity = int(input("Enter the quantity of the product: "))

print("")
del_cost = float(input("Enter the delivery price: "))
disc_percent = float(input("Enter the discount percentage: "))

p1_cost = p1_price * p1_quantity
p2_cost = p2_price * p2_quantity
p3_cost = p3_price * p3_quantity

product_cost = p1_cost + p2_cost + p3_cost
discount = product_cost * disc_percent / 100
discounted_cost = product_cost - discount
cost_with_delivery = discounted_cost + del_cost

print("------------ INVOICE -------------")
print("")
print(p1_name + "---------> "  + str(p1_cost) + "x" + str(p1_quantity) + " >>> " + str(p1_cost))
print(p2_name + "---------> "  + str(p2_cost) + "x" + str(p2_quantity) + " >>> " + str(p2_cost))
print(p3_name + "---------> "  + str(p3_cost) + "x" + str(p3_quantity) + " >>> " + str(p3_cost))
print("")
print("Full cost >>> " + str(product_cost))
print(" Discount >>> " + str(disc_percent) + "%")
print("          >>> " + str(discount))
print("")
print("Discounted Price >>> " + str(discounted_cost))
print(" Delivery Charge >>> " + str(del_cost))
print("           Total >>> " + str(cost_with_delivery))
print("----------------------------------")