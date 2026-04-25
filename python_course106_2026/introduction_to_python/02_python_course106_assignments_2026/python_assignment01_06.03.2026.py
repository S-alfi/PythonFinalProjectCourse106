

# Python assignments:

# Date: 06.03.2026
# Assignment - 01

city_01 = "Tel Aviv"
city_01_value_replace = city_01.replace(" ", "-")

city_02 = "new-york"
city_02_value_replace = city_02.replace("new-york", "New-York")

city_03 = "Rome"
city_04 = "London"

l_city_03 = len(city_03)
l_city_04 = len(city_04)

sentence_01 = "Leo Messi is 30"
sentence_02 = "Leo Messi's age is 30 years old"

index_01 = sentence_01.index("is")
index_02 = sentence_02.index("is")
index_03 = sentence_02.index("years")

only_age_for_sentence_01 = sentence_01[index_01 + 3:]
only_age_for_sentence_02 = sentence_02[index_02 + 3:index_03 - 1]

print()
print(f'1. {city_01_value_replace}')
print(f'2. {city_02_value_replace}')
print(f'3. The length of the string Rome is: {l_city_03}\n   The length of the string London is: {l_city_04}')
print(f'4. Get only age for sentence 01: {only_age_for_sentence_01}')
print(f'5. Get only age for sentence 02: {only_age_for_sentence_02}')

