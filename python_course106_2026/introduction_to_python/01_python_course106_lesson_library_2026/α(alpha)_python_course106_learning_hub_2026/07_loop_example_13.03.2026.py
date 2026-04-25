

# Topic 06: Loops

# A loop in Python is a way to repeat a block of code multiple times until a condition is met.

print()

# An example of boolean variable

first_name = "Mike"
last_name = "Wazowski"
is_first_name_longer = first_name > last_name # is_first_name_longer = Boolean (true or false).


# For each value of i from 0 to 2, return i × 10.

for i in range(0,3):
    i_multiplied_by_10 = i * 10
    print(f'1. The value: {i} multiplied by 10 = {i_multiplied_by_10}')

print()

# For each value of i from 0 to 9, check whether i² is greater than 25 or less than 25.

for i in range(0,10):
    i_squared = i ** 2
    if i_squared > 25:
        print(f'2. The value of {i} squared is greater than 25. i² = {i_squared}')
    elif i_squared == 25:
        print(f'2. The value of {i} squared is equal to 25. i² = {i_squared}')
    else:
        print(f'2. The value of {i} squared is less than 25. i² = {i_squared}')

print()

# In Python, the break statement is used to stop a loop immediately.
# For each value of i from 0 to 19, check whether i² is greater than 25, and return only the first value where i² is greater than 25 (which is 6).

for i in range(0,20):
    i_squared = i ** 2

    if i_squared > 25:
        print(f'3. The value of {i} squared is greater than 25. i² = {i_squared}')
        break

print()

# In Python, the continue statement is used to skip the rest of the code in the current loop iteration and move directly to the next iteration of the loop.
# For each value of i from 0 to 19, check whether i² is greater than 25, and return only the first value where i² is greater than 25 and i != 6 (which is 7).

for i in range(0,20):
    i_squared = i ** 2

    if i == 6:
        continue

    if i_squared > 25:
        print(f'4. The value of {i} squared is greater than 25. i² = {i_squared}')
        break

print()

# This loop finds all pairs of numbers between 0 and 12 whose sum is 12, and prints each pair only once, ensuring that the first number is less than or equal to the second.

for num1 in range(0,13):
    num2 = 12 - num1
    if num1 <= num2:
        print(f'5. Number 1: {num1} , Number 2: {num2}')

print()

# Print the multiplication table of 3 from 0 to 10.

for num2 in range(0,11):
    num1 = 3
    print(f'6. {num1} * {num2} = {num1 * num2}')

print()

# This loop prints the name ‘Mike Hawk’ one character at a time, starting with the first character, and adds one more character in each line until the full name is printed.

name = "Mike Hawk"
l = len(name)

for letter in range(1,len(name)+1):
    sliced_name = name[:letter]
    if sliced_name[-1] != " ":  # Skip slices ending with a space
        print(f'7. {sliced_name}')

print()

# This loop prints the sum of all integers from 2 through 10.

sum_of_numbers_from_2_to_10 = 0

for num in range(2,11):
    sum_of_numbers_from_2_to_10 += num
    if num == 10:
        print(f'8. The sum of all integers from 2 through 10 = {sum_of_numbers_from_2_to_10}')

print()

# This loop prints the sum of all integers from 0 through 10 and the sum of all integers from 10 through 20.

sum_of_numbers_from_0_to_10 = 0
sum_of_numbers_from_10_to_20 = 0

for num in range(0,21):
    if num <= 10:
        sum_of_numbers_from_0_to_10 += num
    if num >= 10:
        sum_of_numbers_from_10_to_20 += num

print(f'9. The sum of all integers from 0 through 10 = {sum_of_numbers_from_0_to_10}')
print(f'9. The sum of all integers from 10 through 20 = {sum_of_numbers_from_10_to_20}')


print("\nDebug button")

