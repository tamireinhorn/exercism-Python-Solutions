from copy import deepcopy
from itertools import zip_longest
import re


def solve(puzzle: str) -> dict[str, int]:
    #   1 
    #  BB
    # 1LL
    # First, we need to split the left and right sides
    new_puzzle = deepcopy(puzzle)
    #avaliable_letters = {letter: -1 for letter in set(re.sub('\+|\s|=', '', puzzle))}]
    avaliable_letters = {}
    elements = re.findall('\w+', puzzle)
    sizes = list(map(len, elements))
    right_side = elements[-1]
    # Is there carryover to the first digit?
    if max(sizes[0:len(sizes)-1]) < sizes[-1]:
        # If there is, since everything is single digit, the first letter of the right side = 1
        avaliable_letters[right_side[0]] = '1'
        new_puzzle = re.sub(right_side[0], '1', deepcopy(puzzle))
        # Due to that carry, we also know that the second digit is 0.
        avaliable_letters[right_side[1]] = 0
        new_puzzle = re.sub(right_side[1], '0', new_puzzle)
    return avaliable_letters


def equation_creation(elements: list[str]):
    pass