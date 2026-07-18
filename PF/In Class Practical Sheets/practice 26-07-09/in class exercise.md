
## 1.
```text
* * * * *
* * * *
* * *
* *
*
```
```python
n = 5
for i in range(5):
    for j in range(n):
        print("*",end=" ")
    n -= 1
    print()
```
```python
i = 5
while i >= 1:
    j = 1
    while j <= i:
        print("*",end=" ")
        j += 1
    i -= 1
    print()
```



| i   | while i >= 1 | j   | while j <= i  | print("\*") | j += 1 | i -= 1 |
| --- | ------------ | --- | ------------- | ----------- | ------ | ------ |
| 5   | True         | 1   | 1 <= 5  True  | \*          | 1+1 =2 | -      |
|     |              | 2   | 2 <= 5  True  | \*\*        | 2+1 =3 | -      |
|     |              | 3   | 3 <= 5  True  | \*\*\*      | 3+1 =4 | -      |
|     |              | 4   | 4 <= 5  True  | \*\*\*\*    | 4+1 =5 | -      |
|     |              | 5   | 5 <= 5  True  | \*\*\*\*\*  | 5+1 =6 | -      |
|     |              | 6   | 6 <= 5  False | -           | -      | 5-1 =4 |
| 4   | True         | 1   | 1 <= 4  True  | \*          | 1+1 =2 | -      |
|     |              | 2   | 2 <= 4  True  | \*\*        | 2+1 =3 | -      |
|     |              | 3   | 3 <= 4  True  | \*\*\*      | 3+1 =4 | -      |
|     |              | 4   | 4 <= 4  True  | \*\*\*\*    | 4+1 =5 | -      |
|     |              | 5   | 5 <= 4  False | -           | -      | 4-1 =3 |
| 3   | True         | 1   | 1 <= 3  True  | \*          | 1+1 =2 | -      |
|     |              | 2   | 2 <= 3  True  | \*\*        | 2+1 =3 | -      |
|     |              | 3   | 3 <= 3  True  | \*\*\*      | 3+1 =4 | -      |
|     |              | 4   | 4 <= 3  False | -           | -      | 3-1 =2 |
| 2   | True         | 1   | 1 <= 2  True  | \*          | 1+1 =2 | -      |
|     |              | 2   | 2 <= 2  True  | \*\*        | 2+1 =3 | -      |
|     |              | 3   | 3 <= 2  False | -           | -      | 2-1 =1 |
| 1   | True         | 1   | 1 <= 1  True  | \*          | 1+1 =2 | -      |
|     |              | 2   | 2 <= 1  False | -           | -      | 1-1 =0 |
| 0   | False        | -   | -             | -           | -      | -      |

# 2. 
```text
*
**
***
****
*****
```

```python
i = 1
while i <= 5:
	j = 1
	while j <= i:
		print("*",end=" ")
		j += 1
	print()
	i += 1
```

| i   | while i <= 5 | j   | while j <= i | print("\*") | j += 1 | i += 1 |
| --- | ------------ | --- | ------------ | ----------- | ------ | ------ |
| 1   | True         | 1   | True         | *           | 1+1=2  | -      |
|     |              | 2   | False        | -           | -      | 1+1=2  |
| 2   | True         | 1   | True         | **          | 1+1=2  | -      |
|     |              | 2   | True         | ***         | 2+1=3  | -      |
|     |              | 3   | False        | -           | -      | 2+1=3  |
| 3   | True         | 1   | True         | *           | 1+1=2  | -      |
|     |              | 2   | True         | **          | 2+1=3  | -      |
|     |              | 3   | True         | ***         | 3+1=4  | -      |
|     |              | 4   | False        | -           | -      | 3+1=4  |
| 4   | True         | 1   | True         | *           | 1+1=2  | -      |
|     |              | 2   | True         | **          | 2+1=3  | -      |
|     |              | 3   | True         | ***         | 3+1=4  | -      |
|     |              | 4   | True         | ****        | 4+1=5  | -      |
|     |              | 5   | False        | -           | -      | 4+1=5  |
| 5   | True         | 1   | True         | *           | 1+1=2  | -      |
|     |              | 2   | True         | **          | 2+1=3  | -      |
|     |              | 3   | True         | ***         | 3+1=4  | -      |
|     |              | 4   | True         | ****        | 4+1=5  | -      |
|     |              | 5   | True         | ****\*      | 5+1=6  | -      |
|     |              | 6   | False        | -           | -      | 5+1=6  |
| 6   | False        | -   | -            | -           | -      | -      |

# Programming Fundamentals – Nested Loops Worksheet (2026 July 9)
## 1. Print a Square Pattern
```python
# Write a program to print a 5 × 5 square using the * symbol.
for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print()
```
## 2. Multiplication Table
```python
# Write a program to display the multiplication tables from 1 to 5. 

i = 1
while i <= 5:
    j = 1
    while j <= 5:
        print(f"{i*j:3}",end=" ")
        j += 1
    print()
    i += 1
```
## 3. Number Grid 
```python
# Write a program to print a 4 × 4 grid containing the numbers 1 to 4 on each row.

i = 1
while i <= 4:
    j = 1
    while j <= 4:
        print(j,end=" ")
        j += 1
    i += 1
    print()
```
## 4. Right Triangle Pattern 
```python
# Write a program to print a right triangle using * with 5 rows.

i = 1
while i <= 5:
    print("*") if i == 1 else print("*",end=" ")
    j = 2
    while j <= i:
        if j == i:
            print("*")
        elif i == 5 and j < 5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j += 1
    i += 1
```
## 5. Classroom Seating Plan 
```python
# A  classroom has 6 rows and each row has 5 desks.
# Display the seating arrangement as: Row 1: Desk1 Desk2 Desk3 Desk4 Desk5.

raw = 1
while raw <= 6:
    print(f"Raw {raw}: ",end="")
    desk = 1
    while desk <= 5:
        print(f"Desk {desk} ",end="")
        desk += 1
    print()
    raw += 1
```
## 6. Ice Cream Shop 
```python
# An ice cream shop has 4 freezers.
# Each freezer contains 6 ice cream boxes.
# Each box contains 20 ice creams. 

# Calculate: 
#   Total number of ice cream boxes. 
#   Total number of ice creams in the shop.

count_icecream = 0
count_box = 0
freezer = 1
while freezer <= 4:
    box = 1
    while box <= 6:
        count_box += 1
        ice = 1
        while ice <= 20:
            count_icecream += 1
            ice += 1
        box += 1
    freezer += 1

print(f"Ice Cream Boxes x {count_box}")
print(f"Ice Creams x {count_icecream}")
```
## 7. School Examination
```python
# A school has 5 classrooms.
# Each classroom has 25 students.
# Each student pays Rs. 500 as the examination fee.

# Calculate:
#   Total number of students.
#   Total examination fee collected.

count = 0
exam_fee = 0
clzroom = 5
while clzroom >= 1:
	student = 25
	while student >= 1:
		count += 1
		exam_fee += 500
		student -= 1
	clzroom -= 1

print(f"Total Number of Students ={count}")
print(f"Total Examination Fee Collected = Rs {exam_fee:,.2f}")
``````
## 8. Orange Farm
```python
# An orange farm has 8 trees.
# Each tree produces 35 oranges.
# Calculate the total number of oranges harvested.

count = 0
tree = 8
while tree >= 1:
	orange = 35
	while orange >= 1:
		count += 1
		orange -= 1
	tree -= 1

print(f"Total Number of Oranges Harvested = {count}")
```
## 9. Hotel classrooms
```python
# A hotel has 6 floors. Each floor has 18 rooms. Each room costs Rs. 12,000 per night. Assume every room is occupied. 

# Calculate: 
#   Total number of rooms. 
#   Total income for one night.

count = 0
income = 0
floor = 6
while floor >= 1:
    room = 18
    while room >= 1:
        count += 1
        income += 12000
        room -= 1
    floor -= 1

print(f"Total number of rooms = {count}")
print(f"Total income for one night = Rs {income:,.2f}")
```
## 10. Airline Passengers
```python
# An airline operates 5 flights. Each flight has 30 rows and each row has 6 seats. Assume every seat is occupied. 

# Calculate: 
#   Number of passengers on one flight. 
#   Total number of passengers on all flights.

passengers = 0
flights = 5
n = flights
while flights >= 1:
    row = 30
    while row >= 1:
        seat = 6
        while seat >= 1:
            passengers += 1
            seat -= 1
        row -= 1
    flights -= 1

print(f"Number of passengers on one flight x {passengers / n:.0f}")
print(f"Total number of passengers on all flights x {passengers}")
```