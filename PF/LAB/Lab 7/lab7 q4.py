# Q4 - ATM Withdrawal System

bal = 50000
total_withdrawn = 0
success = 0
i = 0

while True:
    amount = float(input("Amount: "))
    if amount == -1:
        break
    if amount <= bal:
        bal -= amount
        total_withdrawn += amount
        success += 1
    else:
        print("Insufficient Balance")
    i += 1
print(f"Remaining Balance = Rs.{bal}")
print(f"Total amount withdrawn = Rs.{total_withdrawn}")
print(f"Successful withdrawals = {success}")
    
