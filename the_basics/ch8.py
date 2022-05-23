# Ask for the total price of the bill, then ask how many diners there are. Divide the total bill by the number of diners and show how much each person must pay.

from functools import total_ordering


totalbill = int(input("Enter total bill for meal: "))
diners = int(input("Enter total number of diners: "))

eachpay = totalbill/diners

print(f'Each diner has to pay {eachpay}')
