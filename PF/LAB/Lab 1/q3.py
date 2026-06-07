#Q3 - calculate compound interest

p = float(input("Enter the principal amount: Rs."))
i = float(input("Enter the annual interest rate: %"))
t = int(input("Enter the number of years: "))

CI = p * (1 + (i / 100))**t - p
CI = round(CI, 2)
# round(value, decimal_places) - rounds a number to specificied number of decimals
#                              - not accurate: halfway .5 decimals somtimes will break
#                              - work behavio with float and int data types can be bit confusing
# f"(value:.2f)" - string formatted method (best)
print("Compound Interest is Rs." + str(CI))