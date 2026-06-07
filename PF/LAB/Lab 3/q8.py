# Q8 - Mobile Data Usage Calculator
print("Mobile Data Usage Calculator\n")
usageGB = float(input("Enter the data usage per month (GB): "))
cost_1GB = float(input("Enter the data cost per GB: Rs."))
additional = float(input("Enter the adiitional service charges: Rs."))

datacost = usageGB * cost_1GB
total = datacost + additional

print("\n                 Data cost >>> " + str(datacost))
print("Additional service charges >>> " + str(additional))
print("                Total bill >>> " + str(total))