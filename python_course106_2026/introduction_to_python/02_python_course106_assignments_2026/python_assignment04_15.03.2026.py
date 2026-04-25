

# Python assignments:

# Date: 15.03.2026
# Assignment - 04

print()

# This loop checks whether a number is within the range of 1 to 20 and then verifies its value by counting up until it reaches that number.

random_number = 8
increment = 0

if random_number < 1 or random_number > 20:
    print("1. The random number is outside the range of 1 to 20.")
else:
    while increment <= 20:
        increment += 1
        if increment == random_number:
            print(f'1. The random number is: {random_number}')

print()

# This code checks if a withdrawal would make the balance go below zero. If not, it allows the transaction and prints the remaining balance.
# If the balance goes below zero, it will print: "This total is not permitted."

balance = 1000
transaction = -500
final_balance = balance + transaction

if final_balance < 0:
    print("2. This total is not permitted")
else:
    print(f'2. The total is permitted, and the remaining balance is: {final_balance}')


print("\nDebug button")

