

# Topic 08: Lists

# In Python, a list is an ordered, mutable collection of items that can hold elements of different data types.

print()

first_name_list = ["Liroy", "Rony", "Ofri", "Adele"]
last_name_list = ["Lastname1", "Lastname2", "Lastname3"]
age_list = [20, 23, 24, 34, 56, 23, 70, 67, 45, 34, 56]

# This code returns the length of the list first_name_list, (4).

l_first_name_list = len(first_name_list)

# This code gets the second item from the list first_name_list (index 1), "Rony".

second_item = first_name_list[1]

# This code gets the second last item from the list last_name_list (index -2), "Lastname2".

second_last_item = last_name_list[-2]

# This code slices the list age_list from the item in (index 1) to the item in (index 4) excluded, [23,24,34].

sliced_list = age_list[1:4]

# This code searches for a specific value in the list age_list and returns the index (position) of that value. value = 70, index = 6.

index = age_list.index(70)

# This code slices the list age_list from the item in (index 0) to the item (70) excluded, [20, 23, 24, 34, 56, 23].

sliced_age_list = age_list[0:index]

# In Python, the append() method is used with lists to add a new item to the end of the list.
# This code adds the item "Shay" to the end of the list first_name_list, ["Liroy", "Rony", "Ofri", "Adele", "Shay"]

first_name_list.append("Shay")

# In Python, the insert() method is used with lists to add an item at a specific position (index) in the list.
# This code adds the item "Batel" to (index 3) in the list first_name_list, ["Liroy", "Rony", "Ofri", "Batel", "Adele", "Shay"]

first_name_list.insert(3,"Batel")

# This code checks if the item "Rony" is in the list first_name_list : True

is_roni_in_list = "Rony" in first_name_list

# This code checks if the item "Morgan" is in the list first_name_list : False

is_morgan_in_list = "Morgan" in first_name_list

# This code returns the amount of times the value (23) appears in the list age_list using the count() method, count: 2.

count = age_list.count(23)

# This code goes through the list numbers_list_01 and prints every item one by one.

numbers_list_01 = [23, 45, 65, 12, 20, 45, 67, 98]
l_numbers_list_01 = len(numbers_list_01)

# Version 01

for i in range(l_numbers_list_01):
    print(f'1. {numbers_list_01[i]}')

print()

# Version 02 (preferred option)

for number in numbers_list_01:
    print(f'2. {number}')

print()

# This code goes through the list numbers_list_01 and calculates the sum of all the items within it.

summary = 0

for number in numbers_list_01:
    summary += number
print(f'3. The sum of all the items in the list is: {summary}')

print()

# This code goes through the list city_list and returns the value with the longest length.

city_list = ["Rome", "London", "Paris", "Berlin", "Barcelona", "New-York"]
city_with_the_longest_length = ""

for city in city_list:
    if len(city) > len(city_with_the_longest_length):
        city_with_the_longest_length = city
print(f'4. The city with the longest length is: {city_with_the_longest_length}')

print()

# This code goes through the list numbers_list_02 and separates between the even numbers and the odd numbers.

numbers_list_02 = [0, 1, 2, 3, 4, 5, 6, 7]
even_numbers_list = []
odd_numbers_list = []

# Version 01

even_numbers = [number for number in numbers_list_02 if number % 2 == 0]
odd_numbers = [number for number in numbers_list_02 if number % 2 != 0]
print(f'5. The even numbers are: {even_numbers}')
print(f'5. The odd numbers are: {odd_numbers}')

print()

# Version 02

for number in numbers_list_02:
    if number % 2 == 0:
        even_numbers_list.append(number)
    else:
        odd_numbers_list.append(number)

print(f'5. The even numbers are: {even_numbers_list}')
print(f'5. The odd numbers are: {odd_numbers_list}')

print()

# This code goes through the list emails_list and checks if an item (email) is valid - An email must contain the "@" symbol in order to be valid.

emails_list= ["david@domain.org", "sara.outlook.com", "john@gmail.com"]
for email in emails_list:
    if "@" in email:
        print(f'6. This email is valid, {email}')
    else:
        print("6. This email is invalid.")

print()

# This code goes through the list numbers_list_03 and separates between the numbers above 10 and below 10. If a number = 0, exit the loop.

numbers_list_03 = [3, 5, 13, 12, 0, 78, 4, 23]
numbers_below_10 = []
numbers_above_10 = []

for number in numbers_list_03:
    if number == 0:
        break
    if number < 10:
        numbers_below_10.append(number)
    else:
        numbers_above_10.append(number)

print(f'7. The numbers below 10 are: {numbers_below_10}')
print(f'7. The numbers above 10 are: {numbers_above_10}')


print("\nDebug button")

