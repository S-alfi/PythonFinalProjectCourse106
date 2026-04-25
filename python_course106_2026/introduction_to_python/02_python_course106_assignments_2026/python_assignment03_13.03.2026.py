

# Python assignments:

# Date: 13.03.2026
# Assignment - 03

print()

# This loop prints all the even integers from 0 through 20.

print("1. The even numbers between 0 and 20 are as follows:", end=' ')
for num in range(0, 21):
    if num % 2 == 0:
        print(num, end=' ')

print(f'\n')

# This loop calculates and prints the sum of all even integers from 0 through 20, the sum of all odd integers from 0 through 20, and their combined total.

sum_of_even_numbers_from_0_to_20 = 0
sum_of_odd_numbers_from_0_to_20 = 0

for num in range(0, 21):
    if num % 2 == 0:
        sum_of_even_numbers_from_0_to_20 += num
    else:
        sum_of_odd_numbers_from_0_to_20 += num

total = sum_of_even_numbers_from_0_to_20 + sum_of_odd_numbers_from_0_to_20

print("2. The sum of all even integers from 0 through 20 is:", sum_of_even_numbers_from_0_to_20)
print("2. The sum of all odd integers from 0 through 20 is:", sum_of_odd_numbers_from_0_to_20)
print("2. The total is:", total)


print("\nDebug button")

