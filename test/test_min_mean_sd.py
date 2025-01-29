import unittest

from list_puzzle_solver import ListPuzzleSolver

class TestMinMeanSd(unittest.TestCase):
    def test_mean(self):
        self.assertEqual(
            ListPuzzleSolver([4, -5, 17, -9, 14, 108, -9]).mean(),
            17.142857142857142
        )
        self.assertEqual(
            ListPuzzleSolver([12, -2, 14, 3, -15, 10, -45, 3, 30]).mean(),
            1.1111111111111112
        )
