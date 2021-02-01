
from RomanKata import Convert_Roman
import unittest

class Testing(unittest.TestCase):
    def test_self(self):
        pass

    def test_roman(self):
        numOne = 1
        expected = "I"
        exact = Convert_Roman(numOne)
        self.assertEqual(expected, exact)
    def test_roman(self):
        numFive = 5
        expected = "V"
        exact = Convert_Roman(numFive)
        self.assertEqual(expected, exact)

    def test_roman(self):
        numTen = 10
        expected = "X"
        exact = Convert_Roman(numTen)
        self.assertEqual(expected, exact)

    def test_roman(self):
        numFifty = 50
        expected = "L"
        exact = Convert_Roman(numFifty)
        self.assertEqual(expected, exact)

    def test_roman(self):
        numHundred = 100
        expected = "C"
        exact = Convert_Roman(numHundred)
        self.assertEqual(expected, exact)

    def test_roman(self):
        numFiveHundred = 500
        expected = "D"
        exact = Convert_Roman(numFiveHundred)
        self.assertEqual(expected, exact)

    def test_roman(self):
        numThousand = 1000
        expected = "M"
        exact = Convert_Roman(numThousand)
        self.assertEqual(expected, exact)