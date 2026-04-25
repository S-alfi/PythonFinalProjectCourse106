

# Topic 02: String Operations or String Manipulation

full_name_01 = 'Lionel Messi'
full_name_02 = '   Lionel Messi   '
l = len(full_name_01)
index_01 = full_name_01.index("M")
index_02 = full_name_01.index(" ")


# Note: index values start from 0.
# Example -> 0, 1, 2 etc...


# Find first_name = Lionel by slicing index 0 to index_02 (space) -> index 0 to index 5.

first_name_version_01 = full_name_01[0:index_02]

# Find last_name = Messi by slicing index_02 + 1 (space + 1) all the way to the end of the string.
# -> index 7 to index 12, l = length of full_name_01 = 12.

last_name = full_name_01[index_02 + 1 :l]

# In Python, when you omit the start index in a slice, it defaults to 0.
# [:n] -> from start (0) to index n-1.

first_name_version_02 = full_name_01[:index_02]

# In Python, strip() is a string method that removes whitespace or specified characters from the beginning and end of a string.

full_name_02_strip = full_name_02.strip()

# In Python, lowercase refers to converting all the letters in a string to small letters. You do this using the lower() string method.

full_name_01_lower = full_name_01.lower()

# In Python, uppercase refers to converting all the letters in a string to capital letters. You do this using the upper() string method.

full_name_01_upper = full_name_01.upper()

# In Python, replace() is a string method used to replace a part of a string with another string.

full_name_01_replace = full_name_01.replace("Lionel","Leo")

# In Python, split() is a string method used to break a string into a list of smaller parts based on a separator.

full_name_01_split = full_name_01.split(" ")

print()
print(f'1. The length of {full_name_01} is: {l}')
print(f'2. Get first name version 01: {first_name_version_01}')
print(f'3. Get last name: {last_name}')
print(f'4. When you omit the start index in a slice = index 0,\n   Get first name version 02: {first_name_version_02}')
print()
print(f'5. Get full name using the strip() method: {full_name_02_strip}')
print(f'6. Get full name in small letters using the lower() method: {full_name_01_lower}')
print(f'7. Get full name in capital letters using the upper() method: {full_name_01_upper}')
print(f"8. Replace the value 'Lionel' with 'Leo' in full name using the replace() method: {full_name_01_replace}")
print(f"9. Split full name into two values 'Lionel' and 'Messi' using the split() method: {full_name_01_split}")

