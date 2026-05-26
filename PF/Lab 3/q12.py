# Q12 - Event Budget Planner

print("Event Budget Planner\n")

hall = float(input("Hall Rental: Rs."))
decoration = float(input("Decoration Cost: Rs."))
sound = float(input("Sound System Rental: Rs."))
food_per1 = float(input("Food Cost per person: Rs."))
guests = int(input("Number of Guests: "))

food = guests * food_per1
total = hall + decoration + sound + food

print("\nTotal Event Budget >>> Rs." + str(total))