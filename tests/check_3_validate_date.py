import unittest
import sys
import os

# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))

# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)

# adding the parent directory to
# the sys.path.
sys.path.append(parent)

from src.validate_date import validate_date


# Do not modify the following
# Test Class : code for running the test
class TestDateValidator(unittest.TestCase):
    def setUp(self):
        self.date_list = [
            ("10.12.2000", True, "Valid Date"),
            ("32.12.2000", False, "Date is 32"),
            ("12.32.2000", False, "month is 32"),
            ("13/1/2010", True, "Valid Date"),
            ("25-2-2011", True, "Valid Date"),
            ("00-2-20", False, "Day is 00 and year is 20")
        ]

    def test_dates(self):
        for date in self.date_list:
            with self.subTest(msg=date[0]):
                self.assertTrue(validate_date(date[0]) == date[1], date[0] + " : " + date[2])


if __name__ == '__main__':
    unittest.main()
