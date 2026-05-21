def q1_1():
      print("")
      print("Q1_1 - Calculate the Lucky number using date of birth")
      print("")

      bd = input("Enter date of birth: ")
      F = int(bd)
      n = len(str(F))
      while n > 1:
            if n == 2:
                  F = int(str(F)[0]) + int(str(F)[1])
            n = len(str(F))
      print("date of Birth >>> " + bd
            + "   | Digital Root >>> " + str(F))

      # Pseudocode
      '''
      start
            import dateofbirth
            F = int dateofbirth
            n = len of str F
            while n > 1
                  if n == 2
                        F = int(str(F)[0]) + int(str(F)[1])
                  end if
                  n = len of str F
            end while
            display F
      end
      '''
def q1_2():
      print("")
      print("Q1_2 - Calculate digital root of Any number")
      print("")
      number = int(input("Enter a number(0 < n < ∞): "))
      steps = []
      current = number

      while len(str(current)) > 1:
            digit_sum = 0
            for d in range(len(str(current))):
                  digit_sum = digit_sum + int(str(current)[d])
            steps.append(digit_sum)
            current = digit_sum

      chain = [number] + steps
      print(" > ".join(str(x) for x in chain))

      # digit_sum = sum(int(digit) for digit in str(current))
      #digital_root = 1 + (number - 1) % 9
def q2_1():
      print("")
      print("Q2_1 - Reverse the digit order of a given number using values.(0<digits<5)")
      print("")

      num = input("Enter the number: ")
      n = int(num)
      length = len(str(n))

      if length == 1:
            R = n
      elif length == 2:
            R = (n % 10)*10 + (n // 10)
      elif length == 3:
            R = (n % 10)*100 + (n // 10 % 10)*10+ (n // 100)
      elif length == 4:
            R = (n % 10)*1000 + (n // 10 % 10)*100 + (n // 100 % 10)*10 + (n // 1000)
      elif length == 5:
            R = (n % 10)*10000 + (n // 10 % 10)*1000 + (n // 100 % 10)*100 + (n // 1000 % 10)*10 + (n // 10000)
      else:
            pass
      R = int(R)
      print(str(R))
def q2_2():
      print("")
      print("Q2_2 - Reverse the digit order of any natural number(using loops).(0 < digits < ∞)")
      print("")

      n = int(input("Enter the number: "))
      reversed = 0
      length = len(str(n))

      for r in range(length):
            digit = (n // (10**r)) % 10
            reversed = reversed + digit*(10**(length - r - 1))

      print("Number >>> " + str(n)
            + "  | Reversed >>> " + str(reversed))
      
      '''
      start
            input n
            n = int n
            reversed = 0
            length = len of str n
            for r in range of length
                  digit = (n // (10**r)) % 10
                  reversed = reversed + digit*(10**(length - r - 1))
            end for
            display reversed
      end
      '''

#--------------------------------------------------------------------------------------------

print("1.1 >>> Q1_1 - Calculate the Lucky number using date of birth")
print("1.2 >>> Q1_2 - Calculate digital root of Any number")
print("")
print("2.1 >>> Q2_1 Reverse the digit order of a given number using values.(0 < digits < 5)")
print("2.2 >>> Q2_2 Reverse the digit order of any natural number(using loops) (0 < digits < ∞)")
print("")

program = input("Enter number of prefered program(1, 2.1, ...): ")
if program == "1.1":
      q1_1()
elif program =="1.2":
      q1_2()
elif program == "2.1":
      q2_1()
elif program == "2.2":
      q2_2()
else:
      q1_1()
      q1_2()
      q2_1()
      q2_2()