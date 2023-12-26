n = int(input("Enter a number :"))

#pattern1
print("pattern 1 :")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

#pattern 2:
print("\npattern 2")
for i in range(1, n + 1):
    for _ in range(n - i):
        print(" ", end='')
    
    for j in range(1, i + 1):
        print(j, end='') 
    print()

#pattern 3:
print("\npattern 3:")
for i in range(1, n+1):
    print(" "*(n-i), end="")
    for j in range(1, i+1):
        print(j, end="")
    for j in range(i, 0, -1):
        print(j, end="")
    print("")
#pattern 4:
print("\npattern 4:")
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end='')
    print()

#pattern 5:
print("\npattern 5:")
for i in range(1, n + 1):
    for _ in range(n - i):
        print(" ", end='')
    for j in range(1, i + 1):
        print(j, end='')
    for j in range(i - 1, 0, -1):
        print(j, end='')

    print()

#pattern 6:
print("\npattern 6 :")
for i in range(1, n + 1):
    for _ in range(n - i):
        print(" ", end='')
    for j in range(1, i + 1):
        print(j, end='')
    for j in range(i - 1, 0, -1):
        print(j, end='')

    print()

for i in range(n - 1, 0, -1):
    for _ in range(n - i):
        print(" ", end='')
    for j in range(1, i + 1):
        print(j, end='')
    for j in range(i - 1, 0, -1):
        print(j, end='')

    print()