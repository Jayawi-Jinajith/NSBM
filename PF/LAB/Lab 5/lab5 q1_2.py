# Q1_2 - Voting eligibilty verification
# 1 - age >= 18
# 2 - must be a citizen
# 3 - Valid ID

birth_year = int(input("Enter the birth year: "))
age = 2026 - birth_year
if age >= 18:
    citizen = input("Are you a citizen of Sri Lanka(Yes/No): ")
    if citizen[0].upper() == "Y":
        valid_id = input("Do you have a Valid ID(Yes/No): ")
        if valid_id[0].upper() == "Y":
            print("Eligible to Vote")
        else:
            print("Not Eligible to Vote. No Valid NIC")
    else:
        print("Not Eligible to Vote. Not a Citizen")
else:
    print("Not ELigible to Vote. Less than 18 years age")
