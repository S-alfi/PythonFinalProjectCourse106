

# In Python, input() is a built-in function used to get user input from the keyboard.
# [Important]: The input() function returns whatever the user types as a string, even if the user enters a number.

print()

balance = 1000
print("Please enter the amount of your transaction:")
print()
user_input = input() # Get input from the user
user_input_casting_to_int = int(user_input)
final_balance = balance + user_input_casting_to_int

if final_balance > 0:
    print(f'Your final balance is: {final_balance}')
else:
    print("This total is not permitted!")


print("\nDebug button")

