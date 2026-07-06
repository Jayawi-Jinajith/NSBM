# Q5 - Online Quiz Marks

total = 0
highest = 0
lowest = 100

for i in range(8):
    mark = float(input(f"Marks - Quiz {i+1}: "))
    total += mark
    if mark > highest:
        highest = mark
    if mark < lowest:
        lowest = mark

avg = total / (i+1)
print(f"Total mark = {total}")
print(f"Average = {avg}")
print(f"Highest mark = {highest}")
print(f"Lowest mark = {lowest}")
