

# Topic 07: While - loop

# In Python, a while loop is a type of loop that repeatedly executes a block of code as long as a specified condition is true.
# It is condition-controlled, which means it keeps running until the condition becomes False.

print()

# When you define a loop using a single value in range(), it starts at 0 and iterates up to, but not including, that value.
# An example: range(3) generates numbers starting from 0 up to 3 (excluded) -> 0, 1, 2.

for i in range(3):
    if i < 3:
        print(f'1. The value is = {i}, Using For-loop.')

print()

# [Important]: A while loop must be designed so that it will eventually stop.

i = 0

while i < 5:
    print(f'2. The value is = {i}, Using While-loop.')
    i += 1


print("\nDebug button")

