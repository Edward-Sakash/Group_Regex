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

from src.format_bio import format_bio


# Do not modify the following
# Test Class : code for running the test
class TestBioFormatter(unittest.TestCase):
    def setUp(self):
        self.bio_1 = ("hello world", "Hello world.")
        self.bio_2 = ("I am      freeee", "I am freeee.")
        self.bio_3 = ("bonjour.je m'appelle Rob", "Bonjour. Je m'appelle Rob.")
        self.bio_4 = (
            "  .. euh...   I like sports,   especially water sports such as Water Polo,   Diving, etc... ",
            ".. Euh... I like sports, especially water sports such as Water Polo, Diving, etc..."
        )
        self.bio_5 = ("   hello", "Hello.")

    def test_bio_1(self):
        self.assertEqual(format_bio(self.bio_1[0]), self.bio_1[1])

    def test_bio_2(self):
        self.assertEqual(format_bio(self.bio_2[0]), self.bio_2[1])

    def test_bio_3(self):
        self.assertEqual(format_bio(self.bio_3[0]), self.bio_3[1])

    def test_bio_4(self):
        self.assertEqual(format_bio(self.bio_4[0]), self.bio_4[1])

    def test_bio_5(self):
        self.assertEqual(format_bio(self.bio_5[0]), self.bio_5[1])


if __name__ == '__main__':
    unittest.main()
