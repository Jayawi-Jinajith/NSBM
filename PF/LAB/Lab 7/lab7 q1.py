# Q1 - Electricity Bill Caculator

total = 0
i = 1
bills = []
while i <= 5:
    unit_input = "Units consumed by customer " + str(i) + ": "
    units = float(input(unit_input))

    if units <= 100:
        bill = units * 10
    elif units <= 200:
        bill = (100*10) + (units - 100)*15
    else:
        bill = (100*10) + (100*15) + (units - 200)*20
    
    total += bill
    bills.append("Customer" + str(i) + " >>> Rs." + str(bill))
    i += 1
print("\nElectricity Bill\n")
for text in bills:
    print(text)
print("Total Bill >>> Rs.", total)
