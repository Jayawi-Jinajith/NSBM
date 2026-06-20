# Q1 - Voting eligibilty verification
# 1 - age >= 18
# 2 - must be a citizen

age = int(input("Enter the age(Y): "))
if age >= 18:
    citizen = input("Are you a citizen of Sri Lanka(Yes/No): ")
    if citizen.upper() == "YES":
        print("Eligible to Vote")
    else:
        print("Not Eligible to Vote.\nMust be a citizen to be Eligible to Vote")
else:
    print("Not ELigible to Vote.\nMust be 18 years or above to be Eligible to Vote")

# capitalize() - 1st Letter Capital. rest Simple (Word)
# upper() - All capital (WORD)
# lower() - All simple (word)
