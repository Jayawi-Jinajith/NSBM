# Q10 - Loan Interest & Final Settlement Calculator

print("Loan Interest & Final Settlement Calculator\n")
loan = float(input("Enter the loan amount: Rs."))
interest_percent = float(input("Enter the loan interest percentage (%) (yearly): "))
period = int(input("Enter the time period of repayment (months): "))

interest = loan*(interest_percent / 100)*(period / 12)
final = loan + interest
monthly = final / period

print("\n     Total Interest >>> " + str(interest))
print("      Final Payment >>> " + str(final))
print("Monthly Installment >>> " + str(monthly))