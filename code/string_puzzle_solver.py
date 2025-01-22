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
        depth = 0
        parens = ''
        parens_list = []
        for char in self.string:
            match char:
                case '(':
                    depth += 1
                    parens += char
                case ')':
                    if depth == 0: raise StringPuzzleError("Unmatched parentheses") # too many closes
                    depth -= 1
                    parens += char
                case ' ': continue
                case _:
                    raise StringPuzzleError("Invalid character in string: %s" % char)
            if depth == 0:
                parens_list.append(parens)
                parens = ''
        if depth > 0: # too many opens
            raise StringPuzzleError("Unmatched parentheses")
        return parens_list