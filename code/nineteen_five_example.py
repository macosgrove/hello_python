def count_nineteen_five(the_list):
    return {
        19: the_list.count(19),
        5: the_list.count(5),
    }

def check_nineteen_five(the_list):
    count = count_nineteen_five(the_list)
    return count[19] == 2 and count[5] >= 3
