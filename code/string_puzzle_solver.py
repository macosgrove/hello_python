import re

class StringPuzzleError(Exception):
    pass

class StringPuzzleSolver:
    def __init__(self, the_string):
        self.string = the_string

    def split_string(self, separators=' '):
        return [
            re.split(separators, self.string),
            re.findall(separators, self.string)
            ]

    def match_parentheses(self):
        # This is the official solution provided by https://www.w3resource.com/python-exercises/puzzles/python-programming-puzzles-10.php
        # and it sucks. See failing tests.
        # Initialize an empty list 'ls' to store separate parentheses groups
        ls = []

        # Initialize an empty string 's2' to build individual parentheses groups
        s2 = ""

        # Iterate through each character in the modified 'combined' string (spaces removed)
        for s in self.string.replace(' ', ''):
            # Concatenate the character to 's2'
            s2 += s

            # Check if the count of opening parentheses '(' equals the count of closing parentheses ')'
            if s2.count("(") == s2.count(")"):
                # Append the built parentheses group to the 'ls' list
                ls.append(s2)

                # Reset 's2' to an empty string for the next parentheses group
                s2 = ""

        # Return the list of separate parentheses groups
        return ls