## Write programs to print following

1. `1 2 3 4 5`
   ```python
   n = 1
   while n <= 5:
      print(n)
      n = n + 1
   ```
2. `2 4 6 ... 20`
   ```python
   n = 1
   while n <= 10:
      print(2 * n)
      n = n + 1
   ```
3. `36 30 24 18 12 6 0`
   ```python
   n = 30
   while n >= 0:
      print(n)
      n = n - 6
   ```
4. `25 20 15 ... -25`
   ```python
   n = 5
   while n >= -5:
      print(5*n)
      n = n - 1
   ```
5. `1 4 9 16 25 36 49 64 81 100`
   ```python
   n = 1
   while n <= 10:
      print(n**2)
      n = n + 1
   ```

## Loop practice questions

1. addition of 10 numbers
   ```python
   n = 0
   total = 0
   while n < 10:
      num = int(input("Enter the Number " + str(n+1) + ": "))
      total = total + num
      print(total)
      n = n + 1
   ```
2. find largest number out of 5
   ```python
   n = 1
   max = 0
   while n <= 5:
      num = int(input("Enter the Number " + str(n) + ": "))
      if num > max:
         max = num
      n = n + 1
   print("Largest number is " + str(max))
   ```
3. multiplication table 1-12
   ```python
   num = int(input("Enter the Number: "))
   n = 1
   while n <= 12:
      multiply = num * n
      print(str(num) + " X " + str(n) + " = " + str(multiply))
      n = n + 1
   ```