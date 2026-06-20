# Q5 - Loan Approval System

# 1 - monthly slalry >= Rs.50000.00
# 2 - cedit score >= 700

m_salary = float(input("Enter the monthly salary: Rs."))
if m_salary >= 50000:
    credit = float(input("Enter the credit score: "))
    if credit >= 700:
        print("Qualified for the Loan")
    else:
        print("Not Qualified. Not enough credit score")
else:
    print("Not Qualified. Salary is less than eligible amount")
