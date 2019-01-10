SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3


def check_lists(first_list, second_list):
    if first_list == second_list:
        return EQUAL

    if len(first_list) < len(second_list):
        if _search_sublist(first_list, second_list):
            return SUBLIST
    else:
        if _search_sublist(second_list, first_list):
            return SUPERLIST

    return UNEQUAL


def _search_sublist(small_list, large_list):
    # An empty list will always be a sublist of another list.
    if not small_list:
        return True

    small_list_size = len(small_list)
    for i, j in enumerate(large_list):
        if small_list[0] != large_list[i]:
            continue
        if large_list[i:i + small_list_size] == small_list:
            return True

    return False
