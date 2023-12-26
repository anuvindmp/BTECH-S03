#python program to check if a number given by the user is a palindrome. 

n = input("Enter number :")

if n[::-1] == n:
    print("palindrome")
else:
    print("not palindrome")