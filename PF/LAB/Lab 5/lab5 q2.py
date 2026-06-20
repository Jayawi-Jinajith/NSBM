# Q2 - ATM Cash Withdrawl System

# 1- verify pin (1234)
# 2 - withdrawal amount
# 3 - check balance is enough(20000.00)

pin = "1234"
balance = 20000.00

pin_user = (input("Enter the PIN: "))
if pin_user == pin:
    withd_amount = int(input("Enter the Withdrawal Amount: Rs."))
    if withd_amount <= balance:
        balance = balance - withd_amount
        print("Transaction is proceeding. . . please wait a moment")
        print("New Balance = Rs." + balance)
    else:
        print("Account Balance is not sufficient for transaction")
else:
    print("Invalid PIN. Can't procced with the transaction")
