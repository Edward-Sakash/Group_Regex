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

from src.get_username_from_email import get_username_from_email

# Do not modify the following
# Test Class : code for running the test
class TestGetUsername(unittest.TestCase):
    def setUp(self):
        self.sentences = [
            ("ABC3@gmail.com", "ABC3", "Valid username should be returned"),
            ("XYZ@gmail","XYZ", ""),
            ("NONAme", None, "String doesn't have any email")
        ]

    def test_usernameGetter(self):
        for sentence in self.sentences:
            with self.subTest(msg=sentence[0]):
                self.assertTrue(get_username_from_email(sentence[0]) == sentence[1], sentence[2])


if __name__ == '__main__':
    unittest.main()
