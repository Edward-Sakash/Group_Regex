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

from src.get_numbers import get_numbers


# Do not modify the following
# Test Class : code for running the test
class TestGetNumbers(unittest.TestCase):
    def setUp(self):
        self.sentences = [
            ("The Bill is 50", [50], "List should have one number"),
            ("50 + 50 = 100",[50, 50, 100], "List should have 3 numbers"),
            ("There isn't any number", [], "The list should be of length 0 because there isn't any number in the string"),
            ("$45", [45], "List will contain a value")
        ]

    def test_numberGetters(self):
        for sentence in self.sentences:
            with self.subTest(msg=sentence[0]):
                self.assertTrue(get_numbers(sentence[0]) == sentence[1], sentence[2])


if __name__ == '__main__':
    unittest.main()
