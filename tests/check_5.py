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

from src.validate_email import validate_email


# Do not modify the following
# Test Class : code for running the test
class TestEmailValidator(unittest.TestCase):
    def setUp(self):
        self.email_list = [
            ("bonjour@gmail.com", True, "Correct email. It should have been valid"),
            ("Hallo", False, "No @ character"),
            ("3ds@nintendo.jp", False, "Email address not starting with a letter"),
            ("  mi7rar@kelvin.ca", False, "Email address not starting with a letter"),
            ("Nadir!@yahoo.de", False, "Email contains non valid characters"),
            ("Joe-schmo@marathon..com", False, "2 dots in a row after the @"),
            ("Kipchoge@marathon-tokyo.j", False, "Only one letter after the last ."),
            ("Hulk.hogan@WWE.canaDa", False, "More than 5 characters after the last ."),
            ("jon.snow@students.dci.de", True, "Correct email. It should have been valid"),
        ]

    def test_emails(self):
        for email in self.email_list:
            with self.subTest(msg=email[0]):
                self.assertTrue(validate_email(email[0]) == email[1], email[0] + " : " + email[2])


if __name__ == '__main__':
    unittest.main()
