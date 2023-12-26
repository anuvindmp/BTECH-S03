from math import factorial

n = int(input("Enter a number : "))
x = int(input("Enter a value x : "))

#sequence 1
sum = 1
for i in range(2,n+1):
    sum += 1/factorial(i)
print("sum of sequence 1 :", sum)

#sequence 2
sum2 = x
for i in range(2,n+1):
    sum2 += (x**i)/(factorial(i))
print("sum of sequence 2 :", sum2)
