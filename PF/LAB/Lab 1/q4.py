#Q4 - calculate the final salary with allowance, extra work and tax deduction

bs = float(input("Enter the basic sallary: Rs."))
d = int(input("Enter the number of working days: "))
exH = int(input("Enter the extra hours worked: "))

fs = bs + d*bs*0.05 + exH*250 # fs - final salary
tax = fs * 0.12
fs = fs - tax
print("Salary: Rs." + str(fs))