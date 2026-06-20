# Q8 - Vote Eligibility Checker

# input - age
# if age >= 18, eligible
# if age < 18, not eligible
# if user enter "-1", program stop

while True:
    age = int(input("Enter the Age: "))
    if age == -1:
        print("Program ended")
        break
    if age >= 18:
        print("Eligible to vote")
    else:
        print("Not Eligible to vote")
