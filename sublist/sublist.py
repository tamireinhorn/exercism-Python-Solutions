from enum import Enum, unique
@unique
class ListTypes(Enum):
    SUBLIST = 0
    SUPERLIST = 1
    EQUAL = 2
    UNEQUAL = 3

SUBLIST = ListTypes.SUBLIST
SUPERLIST = ListTypes.SUPERLIST
EQUAL = ListTypes.EQUAL
UNEQUAL = ListTypes.UNEQUAL


def list_containment(list_one, list_two):
    if len(list_two) > len(list_one):
        small_list = list_one
        big_list = list_two
        success = SUBLIST
    else:
        small_list = list_two
        big_list = list_one
        success = SUPERLIST
    small_list_size = len(small_list)
    big_list_size = len(big_list)
    for pointer in range(big_list_size - small_list_size + 1):
        chunk = big_list[pointer:(pointer + small_list_size)]
        if chunk == small_list:
            return success
    return UNEQUAL


def sublist(list_one, list_two):
    # Test for equality:
    if list_one == list_two:
        return EQUAL
    return list_containment(list_one, list_two)
    
