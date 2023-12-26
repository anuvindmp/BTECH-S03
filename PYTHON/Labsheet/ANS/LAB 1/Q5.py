#Write a program to read the number of seconds and print it in the form hr:min:sec.

seconds = int(input("Enter total seconds :"))

minute = seconds // 60
seconds -= minute*60
hour = minute // 60
minute -= hour*60

print(hour,":",minute,":",seconds)