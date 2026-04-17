

# Topic 09: Functions

# In Python, a function is a reusable block of code that performs a specific task.
# Instead of writing the same code multiple times, you can put it in a function and “call” it whenever you need.

print()

# This function calculates the average of a list of numbers and returns it.

def calc_avg(grades):

    total = 0
    l = len(grades)

    for grade in grades:
        total += grade

    avg = total / l

    return avg

# This is an empty function.

def empty_func():
    print("1. This is an empty function.")


class AvgOfGrades:

    grades_a = [60, 45, 88, 92, 78, 72]
    grades_b = [78, 80, 82, 75, 90]


    # Call the function empty_func().

    empty_func()

    print()

    # Call the function calc_avg(grades).

    print(f'2. The average of grades_a is: {calc_avg(grades_a)}')
    print(f'2. The average of grades_b is: {calc_avg(grades_b)}')


print("\nDebug button")

