def count_nineteen_five(the_list):
    return {
        19: len([x for x in the_list if x == 19]),
        5: len([x for x in the_list if x == 5])
    }

def check_nineteen_five(the_list):
    count = count_nineteen_five(the_list)
    return count[19] == 2 and count[5] >= 3
