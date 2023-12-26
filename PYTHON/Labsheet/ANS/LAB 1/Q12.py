n = int(input("Enter a number : "))

print("pattern 1 :")
for i in range(n):
    print(' '*(n-i-1)+'*'*(i+1))

print("\npattern 2 : ")
for i in range(n):
    print(' '*(i)+'*'*(n-i))
    
print("\npattern 3 :")
for i in range(n):
    print(' '*(i)+'* '*(n-i))

print("\npattern 4 :")
for i in range(n):
    print('*'*(i+1)+ ' '*(n-i-1)*2 + '*'*(i+1))

print("\npattern 5 :")
for i in range(n):
    print(' '*(i)+'* '*(n-i))
for i in range(2,n+1):
    print(' '*(n-i)+'* '*(i))