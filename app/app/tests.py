"""
sample tests
"""


from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """test the calc modules"""

    def test_add_numbers(self):
        """Adding numbers together"""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """Substracting numbers"""
        res = calc.subtract(15, 10)
        self.assertEqual(res, 5)
