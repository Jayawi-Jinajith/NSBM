# Q2 - Student Attendance

total = 0
eligible = 0
i = 1
while i <= 10:
    att_input = "Student" + str(i) + " - Attendance Percentage: "
    att_percent = float(input(att_input))
    if att_percent >= 75:
        eligible += 1
    total += att_percent
    i += 1
avg = total / 10
print("Number of students Eligible = ", int(eligible))
print("Number of students Not Eligible = ", int(10 - eligible))
print("Average Attendance of the Class = ", avg, "%")

    
