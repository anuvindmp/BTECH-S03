#Python program that prints all the numbers from 0 to 100 except multiples of 3 or 5.

i = 0
while i<=100:
    if (i%3==0 or i%5==0):
        i+=1
        continue
    print(i)
    i+=1