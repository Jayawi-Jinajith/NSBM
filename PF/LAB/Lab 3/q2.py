# Q2 - Student GPA Calculator

sub1 = int(input("Enter marks of 1st subject: " ))
sub2 = int(input("Enter marks of 2nd subject: " ))
sub3 = int(input("Enter marks of 3rd subject: " ))
sub4 = int(input("Enter marks of 4th subject: " ))

total = sub1 + sub2 + sub3 + sub4
average = total / 4
gpa = average / 25

print("Total: " + str(total))
print("Average: " + str(average))
print("GPA: " + str(gpa))