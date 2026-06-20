birthyear = input("Enter your birth year (yyyy): ")
birthmonth = input("Enter your birth month (mm): ")
birthdate = input("Enter your birth date (dd): ")

by = int(birthyear)
bm = int(birthmonth)
bd = int(birthdate)

def x_value(bm):
      x = {
            1: lambda: 0,
            2: lambda: 4 if ((by % 4) == 0) else 3,
            3: lambda: 4 if ((by % 4) == 0) else 3,
            4: lambda: 4 if ((by % 4) == 0) else 3 + 1,
            5: lambda: 4 if ((by % 4) == 0) else 3,
            6: lambda: 4 if ((by % 4) == 0) else 3 + 2,
            7: lambda: 4 if ((by % 4) == 0) else 3,
            8: lambda: 4 if ((by % 4) == 0) else 3,
            9: lambda: 4 if ((by % 4) == 0) else 3 + 3,
            10: lambda: 4 if ((by % 4) == 0) else 3,
            11: lambda: 4 if ((by % 4) == 0) else 3 + 4,
            12: lambda: 4 if ((by % 4) == 0) else 3,
      }
      return x.get(bm, lambda: None)

x = int(x_value(bm))
days_before_jan1 = (31*(bm - 1)) - x + bd
total_days = days_before_jan1 + (2026 - by)*365 + (2026 - by)/4 + 1 if (by % 4) == 0 else 0
dayweek = total_days % 7

def day_of_week(dayweek):
      day = {
            0: lambda: "Wednesday",
            1: lambda: "Thursday",
            2: lambda: "Friday",
            3: lambda: "Saturday",
            4: lambda: "Sunday",
            5: lambda: "Monday",
            6: lambda: "Tuesday",
      }
      return day.get(dayweek, lambda: None)

d = day_of_week(dayweek)
print(str(by) + "-" + str(bm) + "-" + str(bd) + " >>> " + d )