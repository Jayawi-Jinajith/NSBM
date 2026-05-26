# Q3 - Vehicle Trip Cost Estimator

distance = float(input("Enter distance traveled(km): "))
fuelEff = float(input("Enter fuel efficiecy(liters per km): "))
fuelPrice = float(input("Enter fuel price per liter: Rs."))
highwayCharge = float(input("Enter the highway charges: Rs."))

fuelUsed = distance / fuelEff
fuelCost = fuelUsed * fuelPrice
finalCost = fuelCost + highwayCharge

print("      Fuel used: " + str(fuelUsed))
print("      Fuel cost: " + str(fuelCost))
print("Final Trip Cost: " + str(finalCost))