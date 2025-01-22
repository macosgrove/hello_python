class ListPuzzleSolver:
    def __init__(self, the_list):
        self.list = the_list

    def count_nineteen_five(self):
        return {
            19: self.list.count(19),
            5: self.list.count(5),
        }

    def check_nineteen_five(self):
        count = self.count_nineteen_five()
        return count[19] == 2 and count[5] >= 3
