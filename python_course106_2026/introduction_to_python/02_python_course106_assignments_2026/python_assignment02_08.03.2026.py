

# Python assignments:

# Date: 08.03.2026
# Assignment - 02

print()

# This code splits a full name into the first and last names, compares their lengths, and prints whether the first name or the last name is longer or if they are the same length.

full_name = "John Cena"
space_index = full_name.index(" ")
first_name = full_name[0:space_index]
last_name = full_name[space_index + 1:]

if len(first_name) > len(last_name):
    print("1. The length of the first name is longer.")

elif len(first_name) < len(last_name):
    print("1. The length of the last name is longer.")

else:
    print("1. The first and last names are the same length.")

print()

# Calculate the sum of the digits in a three-digit number.

# Version 01

num1 = 150
if 100 <= num1 <= 999:
    num1_casting_to_str = str(num1)
    sum_of_digits = int(num1_casting_to_str[0]) + int(num1_casting_to_str[1]) + int(num1_casting_to_str[2])
    print(f'2. The sum of 3 digits for the number {num1} is: {sum_of_digits}')

else :
    print(f"2. The number: {num1} doesn't have 3 digits.")


# Version 02

num2 = -150

if 100 <= abs(num2) <= 999:
    num2_absolute = abs(num2) # Converts negative numbers to positive
    hundreds = num2_absolute // 100
    tens = (num2_absolute // 10) % 10
    units = num2_absolute % 10
    sum_3_digits_of_num2_absolute = hundreds + tens + units
    print(f'2. The sum of 3 digits for the number {num2} is: {sum_3_digits_of_num2_absolute}')

else:
    print(f"2. The number: {num2} doesn't have 3 digits.")

print()

# This code takes a date in the format DDDMMMYYYY, extracts the day, month, and year, and then prints a new date with the month first, followed by the day and year.

date = "D08M03Y2026"

date_index_month = date.index("M")
date_index_year = date.index("Y")
get_current_day = date[:date_index_month]
get_current_month = date[date_index_month:date_index_year]
get_current_year = date[date_index_year:]

print(f'3. Original order: {date}\n   New order: {get_current_month}{get_current_day}{get_current_year}')


print("\nDebug button")

