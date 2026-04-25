import unittest

# [Important]: Requirements to run Pytest:

# Pytest only discovers tests if you follow these rules:
# 1. Download Python Package: pytest
# 2. Need to import: import unittest
# 3. Need to use: (unittest.TestCase) inside a class
# 4. File name must include the word test in the beginning or the end, test_file_name.py or file_name_test.py
# 5. The name of a function has to start with the word test for example: def test_summary_passed_test_example(self):
# 6. The name of a class can include the word test (optional) for example: class TestMyFirstPytestTestExample(unittest.TestCase):


class TestMyFirstPytestTestExample(unittest.TestCase):

    def test_summary_passed_test_example(self):

        num1 = 4
        num2 = 6
        summary = num1 + num2
        assert summary == 10, "The summary of num1 + num2 should be 10, the result doesn't match."


    def test_difference_failed_test_example(self):

        num1 = 4
        num2 = 6
        difference = num2 - num1
        assert difference == 3, "The difference of num2 - num1 should be 3, the result doesn't match."


print("\nDebug button")

