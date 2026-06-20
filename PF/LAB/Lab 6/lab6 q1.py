# Q1 - Baggage Weight Checker

# input >> baggage weight (kg)
# if weight <= 20, no charge
# if 20 < weight <= 30, Rs.200 per kg for weight exceed than 20 kg
# if weight > 30, not allowed

baggage_kg = float(input("Weight of the baggage (kg): "))

if baggage_kg <= 20:
    charge = "No charge"
elif baggage_kg <= 30:
    charge = 200 * (baggage_kg - 20)
    charge = "Charge = Rs." + str(charge)
else:
    charge = "Exceed the limit(30kg). Not allowed"

print(charge)
