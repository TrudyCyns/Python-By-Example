# Write a program that will ask for a number of days and then will show how many hours, minutes and seconds are in that number of days.

days = int(input("Enter a number of days: "))
sixty = 60

hours = days * 24
minutes = hours*sixty
seconds = minutes*sixty

print(f'Hours: {hours} hours\nMinutes: {minutes} minutes\nSeconds: {seconds} seconds.')
