# Q11 - Electricity Power Comsumption Analyzer

print("Electricity Power Comsumption Analyzer\n")

applianceW = float(input("Appliance Wattage (kW): "))
Hour_pday = float(input("Hours used per day (H): "))
per_kWh = float(input("Cost per kWh: "))

total = applianceW * Hour_pday * 30
total_bill = total * per_kWh

print("Total Electricity Comsumption >>> " + str(total))
print("                   Total Bill >>> " + str(total_bill))