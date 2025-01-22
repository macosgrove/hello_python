import re

class StringPuzzleSolver:
    def __init__(self, the_string):
        self.string = the_string

    def split_string(self, separators=' '):
        return [
            re.split(separators, self.string),
            re.findall(separators, self.string)
            ]
