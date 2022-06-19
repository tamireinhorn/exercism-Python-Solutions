from copy import deepcopy
from itertools import zip_longest
import re
def solve(puzzle: str) -> dict[str, int]:
    #   1 
    #  BB
    # 1LL
    # First, we need to split the left and right sides
    new_puzzle = deepcopy(puzzle)
    avaliable_letters = {letter: -1 for letter in set(re.sub('\+|\s|=', '', puzzle))}
    left_side, right_side = [i.strip() for i in puzzle.split('==')]
    left_side_elements = [i.strip() for i in left_side.split('+')]
    left_side_sizes = list(map(len, left_side_elements))
    # Is there carryover to the first digit?
    if max(left_side_sizes) < len(right_side):
        # If there is, since everything is single digit, the first letter of the right side = 1
        avaliable_letters[right_side[0]] = 1
        new_puzzle = re.sub(right_side[0], '1', deepcopy(puzzle))
        # Due to that carry, we also know that the second digit is 0.
        avaliable_letters[right_side[1]] = 0
        new_puzzle = re.sub(right_side[1], '0', new_puzzle)

    return avaliable_letters
