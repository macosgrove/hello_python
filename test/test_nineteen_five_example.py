from nineteen_five_example import count_nineteen_five
from nineteen_five_example import check_nineteen_five
import unittest

class PrimeNumberTestCase(unittest.TestCase):
    def test_count_nineteen_five(self):
        list = [19, 5, 5, 3, 19, 21, 19]
        self.assertTrue(count_nineteen_five(list) == {19: 3, 5: 2})
        self.assertTrue(count_nineteen_five([]) == {19: 0, 5: 0})

    # Define a test method 'test_non_prime_numbers' to test non-prime numbers.
    def test_check_nineteen_five(self):
        self.assertFalse(check_nineteen_five([]))
        self.assertTrue(check_nineteen_five([19, 19, 15, 5, 3, 5, 5, 2]))
        self.assertFalse(check_nineteen_five([19, 15, 15, 5, 3, 3, 5, 2]))
        self.assertTrue(check_nineteen_five([19, 19, 5, 5, 5, 5, 5]))