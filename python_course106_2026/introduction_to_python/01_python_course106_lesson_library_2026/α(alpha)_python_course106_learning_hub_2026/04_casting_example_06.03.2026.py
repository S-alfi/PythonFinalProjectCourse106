

# Topic 03: Type Casting

# Casting a string variable to an integer variable.

num1 = '12'
num1_casting_to_int = int(num1)
summary = num1_casting_to_int + 4

# Casting an integer variable to a string variable.

num2 = 345
num2_casting_to_str = str(num2)
num2_final = num2_casting_to_str.replace('5', '5$')

print()
print(f'1. The sum of num1_casting_to_int + 4 is: {summary}')
print(f'2. The result of num2_final is: {num2_final}')

