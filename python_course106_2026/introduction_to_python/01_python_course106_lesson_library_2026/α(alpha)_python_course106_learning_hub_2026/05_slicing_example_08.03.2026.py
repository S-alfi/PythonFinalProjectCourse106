

# Topic 04: Slicing

# Get only age for sentence 01.

sentence_01 = "Donald Trump is 79"
index_01 = sentence_01.index("is")

# In Python, if you omit the end index in a slice, the slice continues to the end of the sequence.

default_only_age_for_sentence_01 = sentence_01[index_01 + 3: len(sentence_01)]
shortcut_only_age_for_sentence_01 = sentence_01[index_01 + 3:]

# Get only city for sentence 02.

sentence_02 = "My name is Shay and I live in Ariel"
index_02 = sentence_02.index('in')
only_city_for_sentence_02 = sentence_02[index_02 + 3:]

# Get only age for sentence 03.

sentence_03 = "I am 26 years old"

# Version 01

index_03 = sentence_03.index('am')
index_04 = sentence_03.index('years')
version_01_only_age_for_sentence_03 = sentence_03[index_03 + 3: index_04 - 1]

# Version 02

index_05 = sentence_03.index('am') + 3
version_02_only_age_for_sentence_03 = sentence_03[index_05:index_04]
version_02_only_age_for_sentence_03_stripped = version_02_only_age_for_sentence_03.strip()

# Casting age as a string variable to an integer variable.

version_01_only_age_for_sentence_03_casting_to_int = int(version_01_only_age_for_sentence_03)

# In Python, count() is a method used to count how many times a value appears in a sequence.

get_letter_a_counter_for_sentence_03 = sentence_03.count('a')

print()
print(f'1. Get only age for sentence 01 (default way): {default_only_age_for_sentence_01}')
print(f'2. Get only age for sentence 01 (shortcut way): {shortcut_only_age_for_sentence_01}')
print(f'3. Get only city for sentence 02: {only_city_for_sentence_02}')
print(f'4. Get only age for sentence 03 Version 01: {version_01_only_age_for_sentence_03}')
print(f'5. Get only age for sentence 03 Version 02: {version_02_only_age_for_sentence_03_stripped}')
print(f'6. Get only age for sentence 03 as an integer variable: {version_01_only_age_for_sentence_03_casting_to_int}')
print(f"7. Get the amount of times the letter 'a' appears in sentence 03 using the count() method: {get_letter_a_counter_for_sentence_03}")

