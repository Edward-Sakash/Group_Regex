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

from src.validate_phone_num import validate_phone_num

# Do not modify the following
# Test Class : code for running the test
class TestPhoneNumValidator(unittest.TestCase):
    def setUp(self):
        self.phone_list = [
            ("+1 (44) 444 4444", True, "Number is valid"),
            ("1 (44) 444 4444",False, "No + symbol at starting"),
            ("+1 (475)4444444", False, "No Spaces between numbers after )"),
            ("+1 44 444 4444", False, "area code not enclosed in ()"),
            ("+1(457)7454515", False, "No Spaces between numbers"),
            ("+1 (457) 545 545", False, "1 digit less in last portion of number")
        ]

    def test_phone_nums(self):
        for phone_num in self.phone_list:
            with self.subTest(msg=phone_num[0]):
                self.assertTrue(validate_phone_num(phone_num[0]) == phone_num[1], phone_num[2])


if __name__ == '__main__':
    unittest.main()
