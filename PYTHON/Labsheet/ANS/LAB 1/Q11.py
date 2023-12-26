#strong number
from math import factorial

num = int(input("Enter a number: "))
sum = 0

for i in str(num):
    digit = int(i)
    sum += factorial(digit)

if sum == num:
    print("Strong number")
else:
    print("Not a strong number")
