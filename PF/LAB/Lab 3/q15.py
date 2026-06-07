# Q15 - FreeLancer Income Calculator

print("FreeLancer Income Calculator\n")

projects_count = int(input("Number of Projects: "))
payment_per1 = float(input("Payement per Project: "))
commission_percent = float(input("Platform Commission Percentage (%): "))
tax_percent = float(input("Tax Percentage (%): "))

projects = projects_count * payment_per1
commission = projects * commission_percent / 100
tax = (projects - commission)* tax_percent / 100
total = projects - commission - tax

print("Monthly Earning >>> " + str(total))