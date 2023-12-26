#LEAP YEAR 
year = int(input("Enter an year : "))
if (year%4 == 0 and year%100 !=0) or (year%400 ==0):
    print("LEAP YEAR IT IS !!!!")
else :
    print("NOT LEAP YEAR")