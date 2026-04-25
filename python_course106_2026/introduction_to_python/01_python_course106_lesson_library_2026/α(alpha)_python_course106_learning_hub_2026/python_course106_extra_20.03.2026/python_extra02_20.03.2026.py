

# This code prompts the user to enter a number between 0 and 20 and then uses a while loop to count up to and print that number.

print()

print("Please enter a random number between 0 and 20:")
user_input = input()
user_input_casting_to_int = int(user_input)
print()

if user_input_casting_to_int < 0 or user_input_casting_to_int > 20:
    print("The number is outside the given range.")

elif user_input_casting_to_int == 0:
    print(f'The number is: {user_input_casting_to_int}')

else:

    increment = 0

    while not increment == user_input_casting_to_int:
        print(f'The number is not: {increment}')
        increment += 1
        if increment == 21:
            break
    print(f'The number is: {increment}')


print("\nDebug button")

