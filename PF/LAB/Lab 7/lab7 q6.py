# Q6 - Password Validation

password = "python123"

for attempt in range(3):
    user = input("Enter the Password: ")
    if user == password:
        print(f"Access Gained. ({attempt+1} Attempts)")
        break
    if attempt == 2:
        print(f"Account Locked. ({attempt+1} Attempts)")
