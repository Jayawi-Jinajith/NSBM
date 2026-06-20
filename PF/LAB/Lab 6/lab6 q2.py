# Q2 - Bonus Salary calculator

# input - employee's salary
# if salary >= 100000, bonus 15%
# if 100000 > salary >= 50000, bonus 10%
# if salary < 50000, bonus 5%

salary = float(input("Employee's Salary: Rs."))

if salary >= 100000:
    bonus_rate = 15
elif salary >= 50000:
    bonus_rate = 10
else:
    bonus_rate = 5

bonus = salary * bonus_rate / 100
total = salary + bonus

print("      Salary >>> Rs." + str(salary))
print("       Bonus >>> Rs." + str(bonus) + "  (" + str(bonus_rate) + "%)")
print("Total salary >>> Rs." + str(total))
