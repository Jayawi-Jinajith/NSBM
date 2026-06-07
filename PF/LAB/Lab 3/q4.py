# Q4 - Employee Payroll System

basic = float(input("Enter the basic salary: Rs."))
overtimeHours = float(input("Enter the overtime hours worked: "))
overtimeRate = float(input("Enter the overtime rate: "))
bonus = float(input("Enter the bonus salary: Rs."))
taxPercent = float(input("Enter the tax percentage: "))

overtime = overtimeHours * overtimeRate
grossSalary = basic + overtime + bonus
tax = grossSalary * taxPercent / 100
netSalary = grossSalary - tax

print("Gross Salary: " + str(grossSalary))
print("         Tax: " + str(tax))
print("  Net Salary: " + str(netSalary))