# Q14 - Construction Material Cost Estimator

print("Construction Material Cost Estimator\n")

cement_cost = float(input("Cement Bag price: "))
cement_count = int(input("Cement Bag count: "))
sand = float(input("Sand cost: "))
labor = float(input("Labor Cost: "))
transport = float(input("Transportation Cost: "))

cement = cement_cost * cement_count
total = cement + sand + labor + transport

print("Estimated Construction Cost >>> " + str(total))