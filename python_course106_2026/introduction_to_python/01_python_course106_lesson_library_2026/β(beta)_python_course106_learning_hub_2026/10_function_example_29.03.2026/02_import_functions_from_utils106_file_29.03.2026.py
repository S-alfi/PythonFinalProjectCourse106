from utils106 import Utilities106

# [Important]: Requirements for importing functions from a different file:

# Note: In Python projects, functions are often imported from a file called utils.py

# Note: When you hold Ctrl and left-click on a function name in PyCharm, it typically does the following:
# It takes you directly to its definition, either within the same file or in a different file.

# Steps:
# 1. Need to import: from [file_name] import [class_name], for example: from [utils106] import [Utilities106]
# 2. Need to create an instance of the class in the importing file, for example: utils_106 = Utilities106()
# 3. Functions can be called through an instance, for example: utils_106.empty_func()


grades_a = [60, 45, 88, 92, 78, 72]
grades_b = [78, 80, 82, 75, 90]

utils_106 = Utilities106()  # Instance

print()

# Calling the empty_func(self): function from the utils106.py file.

utils_106.empty_func()

print()

# Calling the calc_avg(self, grades): function from the utils106.py file.

avg_of_grades_a = utils_106.calc_avg(grades_a)
print(f'2. The average of grades_a is: {avg_of_grades_a}')

avg_of_grades_b = utils_106.calc_avg(grades_b)
print(f'2. The average of grades_b is: {avg_of_grades_b}')

print()

if avg_of_grades_a > avg_of_grades_b:
    print("3. The average of grades_a is higher than the average of grades_b.")
elif avg_of_grades_a < avg_of_grades_b:
    print("3. The average of grades_a is lower than the average of grades_b.")
else:
    print("3. The average of grades_a and grades_b are equal.")

print()

# Calling the print_text(self, text): function from the utils106.py file.

utils_106.print_text("4. Test end")

print()

# Calling the print_default_text(self, text="5. Default text"): function from the utils106.py file.

utils_106.print_default_text()

print()

# Calling the calc_avg_of_three_nums(self, num1, num2, num3): function from the utils106.py file.

avg_of_three_nums = utils_106.calc_avg_of_three_nums(23, 45, 67)
print(f'6. The average of the three numbers is: {avg_of_three_nums}')


print("\nDebug button")

