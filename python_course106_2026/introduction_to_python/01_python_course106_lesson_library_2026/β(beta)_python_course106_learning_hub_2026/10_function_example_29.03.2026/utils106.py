

class Utilities106:

    def calc_avg(self, grades):

        if not grades:
            return None

        total = 0
        l = len(grades)

        for grade in grades:
            total += grade

        avg = total / l

        return avg


    def empty_func(self):
        print("1. This is an empty function.")


    def print_text(self, text):
        print(text)


    def print_default_text(self, text="5. Default text"):
        print(text)


    def calc_avg_of_three_nums(self, num1, num2, num3):
        avg = (num1 + num2 + num3) / 3
        return avg

