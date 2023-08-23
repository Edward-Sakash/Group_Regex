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

from src.validate_password import validate_password


# Do not modify the following
# Test Class : code for running the test
class TestPasswordValidator(unittest.TestCase):
    def setUp(self):
        self.password_list = [
            ("aa", False, "Rejected: Password too short"),
            ("012345678901234567890123456789x", False, "Rejected: Password too long"),
            ("az8*!_.-", False, "Rejected: Password not containing any uppercase letter"),
            ("AZ8*!_.-", False, "Rejected: Password not containing any lowercase letter"),
            ("AZa*!_.-", False, "Rejected: Password not containing any digit"),
            ("AbcdEFff3889", False, "Rejected: Password not containing any special character"),
            ("Bo/4512ao*", False, "Rejected: Password containing not permitted character"),
            ("Madisson45!", True, "Accepted Password"),
            ("Secr3t_W0rds", True, "Accepted Password"),
        ]

    def test_passwords(self):
        for psswd in self.password_list:
            with self.subTest(msg=psswd[0]):
                self.assertTrue(validate_password(psswd[0]) == psswd[1], psswd[0] + " : " + psswd[2])


if __name__ == '__main__':
    unittest.main()
