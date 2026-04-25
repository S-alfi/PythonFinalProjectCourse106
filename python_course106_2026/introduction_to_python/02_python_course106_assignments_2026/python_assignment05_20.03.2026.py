

# Python assignments:

# Date: 20.03.2026
# Assignment - 05

print()

# This code loops through a list of months, stops if it finds an invalid month outside range(1,13),
# It adds 5 to the total whenever the month is 9, adds 1 for any other valid month, and then prints the total.

class CommissionCalculateByMonth:

    months_list = [1, 4, 5, 7, 11, 9, 6, 9, 10, 9, 9]
    commission_of_month_9 = 0
    commission_of_other_months = 0

    for month in months_list:
        if month > 12 or month < 1:
            break
        if month == 9:
            commission_of_month_9 += 5
        else:
            commission_of_other_months += 1

    total = commission_of_month_9 + commission_of_other_months

    print(f'   The commission of month 9 is: {commission_of_month_9}')
    print(f'   The commission of the other months is: {commission_of_other_months}')
    print(f'\n1. The total commission is: {total}')

print()

# This code goes through a list of dates and counts how many times a specific month appears.
# If that month appears more than twice, the commission is set to 0; otherwise, the commission is set to 5.

class CommissionCalculateByMonthInFullDate:

    dates_list = ["10.11.2024", "14.07.2024", "18.09.2024", "08.09.2024", "12.01.2024", "03.09.2024"]

    exp_month = "09"
    appearance_of_month_counter = 0


    for date in dates_list:
        parts = date.split(".")
        month = parts[1]
        if month == exp_month:
            appearance_of_month_counter += 1

    if appearance_of_month_counter > 2:
        commission = 0

    else:
        commission = 5

    print(f'2. The commission is: {commission}')


print("\nDebug button")

