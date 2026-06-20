# Q4 - Online Examination Access System

# 1 - student: registered
# 2 - examination fee: paid

registered =input("Is the Student Registered? (Yes/No): ")
if registered[0].upper() == "Y":
    exam_fee = input("Examination Fee is paid? (Yes/No): ")
    if exam_fee[0].upper() == "Y":
        print("Can access Online Examination")
    else:
        print("Cannot access online exam. Examination fee hasn't paid yet")
else:
    print("Cannot access online exam. Student has not registered")
