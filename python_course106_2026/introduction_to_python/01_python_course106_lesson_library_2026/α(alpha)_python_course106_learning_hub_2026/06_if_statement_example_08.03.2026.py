

# Topic 05: If Statement

# In Python, an if statement is a conditional statement used to execute code only when a condition is true.

print()

age = 26

if age > 16:
    print("1. Age is above 16")

else:
    print("1. Age is below 16")

print()

# Exercise 01 - if price_01 > 50, return price_01 + 15% else return price_01 + 10%.

price_01 = 20

if price_01 > 50:
    price_01_over_50_extra_15_precent = price_01 + (15 * price_01) / 100
    print(f'2. The new price for price_01 is: {price_01_over_50_extra_15_precent} |+15%|')

else:
    price_01_below_50_extra_10_precent = price_01 + (10 * price_01) / 100
    print(f'2. The new price for price_01 is: {price_01_below_50_extra_10_precent} |+10%|')

print()

# Exercise 02 - if price_02 > 50, return price_02 + 15% else return price_02 + 10%.

price_02 = "60$"

# In Python, if you want to replace something with “nothing”, you use an empty string "" as the replacement.

price_02 = price_02.replace("$", "") # ("") = nothing
price_02_casting_to_int = int(price_02)

if price_02_casting_to_int > 50:
    price_02_casting_to_int_over_50_extra_15_precent = price_02_casting_to_int + (15 * price_02_casting_to_int) / 100
    print(f'3. The new price for price_02 is: {price_02_casting_to_int_over_50_extra_15_precent} |+15%|')

else:
    price_02_casting_to_int_below_50_extra_10_precent = price_02_casting_to_int + (10 * price_02_casting_to_int) / 100
    print(f'3. The new price for price_02 is: {price_02_casting_to_int_below_50_extra_10_precent} |+10%|')

print()

# Extra - Get the value 2055 as an integer from price_03 (string).

price_03 = "20abcde55$"

price_03_prefix = price_03[:2] # Get prefix = '20'
price_03 = price_03.replace("$", "")
price_03_suffix = price_03[-2:] # Get suffix = '55'
price_03 = price_03_prefix + price_03_suffix
price_03_casting_to_int = int(price_03) # Casting price_03 into integer
print(f'4. The value of price_03 is: {price_03_casting_to_int}')

print()

# In Python, elif is short for “else if”.
# It is used in conditional statements to check multiple conditions in order after the initial if.

price_04 = 200

if price_04 > 80:
    print("5. The price is above 80")

elif price_04 > 50:
    print("5. The price is above 50")

else:
    print("5. The price is below 50")

print()

# Exercise 03 - Check whether the average of three grades is above 90, above 75, above 45, or below these values.

grade_01 = 80
grade_02 = 90
grade_03 = 50

avg_of_3_grades = (grade_01 + grade_02 + grade_03) / 3

if avg_of_3_grades > 90:
    print("6. The average of three grades is above 90.")

elif avg_of_3_grades > 75:
    print("6. The average of three grades is above 75.")

elif avg_of_3_grades > 45:
    print("6. The average of three grades is above 45.")

else:
    print("6. The average of three grades is below 45.")

print()

# Exercise 04 - Determine which string is longer.

city_01 = "Rome"
city_02 = "London"

city_01_length = len(city_01)
city_02_length = len(city_02)

if city_01_length > city_02_length:
    print(f"7. {city_01}'s length is longer, Length = {city_01_length}.")

elif city_01_length < city_02_length:
    print(f"7. {city_02}'s length is longer, Length = {city_02_length}.")

else:
    print("7. Both strings have the same length.")

print()

# Exercise 05 - Test whether the email address is valid.

email_01 = "examplegmail.com"
email_02 = "example@gmail"
email_03 = "example@gmail.com"

# The first method:

if "@" in email_01 and email_01.endswith(".com"):
    print("8. Email_01 is valid")
else:
    print("8. Email_01 is not valid")

if "@" in email_02 and email_02.endswith(".com"):
    print("8. Email_02 is valid")
else:
    print("8. Email_02 is not valid")

if "@" in email_03 and email_03.endswith(".com"):
    print("8. Email_03 is valid")
else:
    print("8. Email_03 is not valid")

print()

# The second method:

emails = ["examplegmail.com", "example@gmail", "example@gmail.com"]

for email in emails:
    if "@" in email and email.endswith(".com"):
        print(f'9. {email} is valid')
    else:
        print(f'9. {email} is not valid')


print("\nDebug button")

