# Q4 - Student mark 

mark = int(input("Student Marks: "))

if mark >= 50:
    result = "Pass"
else:
    result = "Fail"

print(result + " (Marks - " + str(mark) + ")")
