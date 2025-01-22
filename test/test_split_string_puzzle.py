import unittest
from string_puzzle_solver import StringPuzzleSolver

# https://www.w3resource.com/python-exercises/puzzles/index.php
# 8. Split String into Words and Separators

class SplitStringTestCase(unittest.TestCase):
    def test_split_string(self):
        self.assertEqual(
            [['W3resource', 'Python', 'Exercises.'], [' ', ', ']],
            StringPuzzleSolver('W3resource Python, Exercises.').split_string('[,| ]+'),
        )

        self.assertEqual(
            [['The', 'dance', 'held', 'in', 'the', 'school', 'gym', 'ended', 'at', 'midnight.'],
             [' ', ', ', ' ', ' ', ' ', ' ', ', ', ' ', ' ']],
            StringPuzzleSolver('The dance, held in the school gym, ended at midnight.').split_string('[,| ]+'),
        )

        self.assertEqual(
            [['The', 'colors', 'in', 'my', 'studyroom', 'are', 'blue', 'green', 'and', 'yellow.'],
             [' ', ' ', ' ', ' ', ' ', ' ', ', ', ', ', ' ']],
            StringPuzzleSolver('The colors in my studyroom are blue, green, and yellow.').split_string('[,| ]+'),
        )