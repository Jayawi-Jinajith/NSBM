#Q1 - calculate the average marks of 5 students

mark1 = int(input("Enter mark of student 1: "))
mark2 = int(input("Enter mark of student 2: "))
mark3 = int(input("Enter mark of student 3: "))
mark4 = int(input("Enter mark of student 4: "))
mark5 = int(input("Enter mark of student 5: "))
# can use float() or int() - type casting
total = mark1 + mark2 + mark3 + mark4 + mark5
avg = total / 5
print("Total: " + str(total)
      + "  | Average: " + str(avg))