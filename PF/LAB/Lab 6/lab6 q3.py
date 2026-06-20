# Q3 - Calculate sum of numbers from 1 to 10

import time

sum = 0
i = 1

while i <= 10:
    if i == 10:
        print(str(i), end=" ", flush=True)
    else:
        print(str(i), "+ ", end=" ", flush=True)
    time.sleep(0.5)
    sum = sum + i
    i = i + 1
print("\n= ", str(sum))
