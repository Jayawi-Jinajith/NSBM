# Q8 - Grade Classification

# >= 75 : A
# 65-74 : B
# 50-64 : C
# < 50  : F

mark = int(input("Enter student mark: "))
if mark >= 75:
    grade = "A"
elif mark >= 65:
    grade = "B"
elif mark >= 50:
    grade = "C"
else:
    grade = "F"

print("Grade >>> " + grade)
