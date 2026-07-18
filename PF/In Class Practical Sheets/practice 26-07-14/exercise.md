# 
## 1. Factorial Calculation
```python
# Calculate Factorial of a Number

num = int(input("Number: "))
n = num
factorial = 1

while n >= 1:
    factorial *= n
    n -= 1

print(f"{num}! = {factorial}")
```
|num|n  |factorial|n >= 1    |factorial *= n|n -= 1|output|
|---|---|---------|----------|--------------|------|------|
|5  |5  |1        |5>=1 True |1*5=5         |5-1=4 |-     |
|4  |4  |5        |4>=1 True |5*4=20        |4-1=3 |-     |
|3  |3  |20       |3>=1 True |20*3=60       |3-1=2 |-     |
|2  |2  |60       |2>=1 True |60*2=120      |2-1=1 |-     |
|1  |1  |120      |1>=1 True |120*1=120     |1-1=0 |-     |
|0  |0  |120      |0>=1 False|-             |-     |120   |

## 2. Check whether a Number is prime or not
```python
# if number of factors are equal to 2, number is prime

num = int(input("Number: "))
i = num
factor = 0

while i >= 1:
    if num % i == 0:
        factor += 1
    i -= 1

print(f"Factors x {factor}")
if factor == 2:
    print("Prime Number")
else:
    print("Not A Prime Number !")
```
|num|i|factor|i>=1      |num%i==0   |factor+=1|i-=1 |output       |
|---|-|------|----------|-----------|---------|-----|-------------|
|4  |4|0     |4>=1 True |4%4=0 True |0+1=1    |4-1=3|-            |
|-  |3|1     |3>=1 True |4%3=1 False|-        |3-1=2|-            |
|-  |2|1     |2>=1 True |4%2=0 True |1+1=2    |2-1=1|-            |
|-  |1|2     |1>=1 True |4%1=0 True |2+1=3    |1-1=0|-            |
|-  |0|3     |0>=1 False|-          |-        |-    |"Not A Prime"|