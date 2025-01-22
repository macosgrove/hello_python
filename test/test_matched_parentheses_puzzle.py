import unittest
from string_puzzle_solver import StringPuzzleSolver, StringPuzzleError

# https://www.w3resource.com/python-exercises/puzzles/index.php
# 10. Split Matched Parentheses Groups

class MatchParenthesesTestCase(unittest.TestCase):
    def test_match_parentheses(self):
        self.assertEqual(
            ['()'],
            StringPuzzleSolver('( )').match_parentheses()
        )
        self.assertEqual(
            ['(())', '((()()()))', '(())', '()'],
            StringPuzzleSolver('( ()) ((()()())) (()) ()').match_parentheses()
        )
        self.assertEqual(
            ['()', '((()()()))', '(())'],
            StringPuzzleSolver('() (( ( )() ( )) ) ( ())').match_parentheses()
        )
        # The official solution has no error handling so I'll assume it ought to return an empty list in the following cases
        self.assertEqual(
            [],
            StringPuzzleSolver('(').match_parentheses()
        )
        self.assertEqual(
            [],
            StringPuzzleSolver(')(').match_parentheses()
        )
        self.assertEqual(
            [],
            StringPuzzleSolver('(?)').match_parentheses()
        )

