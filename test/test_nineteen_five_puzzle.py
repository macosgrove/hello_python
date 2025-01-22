from list_puzzle_solver import ListPuzzleSolver
import unittest

# https://www.w3resource.com/python-exercises/puzzles/index.php
# 1. Check Nineteen and Five Occurrences

class CountNineteenFiveTestCase(unittest.TestCase):
    def test_count_nineteen_five(self):
        self.assertTrue(ListPuzzleSolver([19, 5, 5, 3, 19, 21, 19]).count_nineteen_five() == {19: 3, 5: 2})
        self.assertTrue(ListPuzzleSolver([]).count_nineteen_five() == {19: 0, 5: 0})

    # Define a test method 'test_non_prime_numbers' to test non-prime numbers.
    def test_check_nineteen_five(self):
        self.assertFalse(ListPuzzleSolver([]).check_nineteen_five())
        self.assertTrue(ListPuzzleSolver([19, 19, 15, 5, 3, 5, 5, 2]).check_nineteen_five())
        self.assertFalse(ListPuzzleSolver([19, 15, 15, 5, 3, 3, 5, 2]).check_nineteen_five())
        self.assertTrue(ListPuzzleSolver([19, 19, 5, 5, 5, 5, 5]).check_nineteen_five())