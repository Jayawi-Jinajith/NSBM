# Q4 - Total, average of 10 marks & pass/fail

total = 0
i = 1

while i <= 10:
    mark_input = "Mark " + str(i) + ": "
    mark = int(input(mark_input))
    total = total + mark
    i = i + 1
average = total / i
if average < 50:
    print("Fail")
else:
    print("Pass")
