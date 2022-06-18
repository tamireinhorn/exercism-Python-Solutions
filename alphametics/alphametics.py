import re
def solve(puzzle: str) -> dict[str, int]:
    #   I 
    #  BB
    # ILL
    # First, we need to split the left and right sides
    avaliable_letters = {letter: -1 for letter in set(re.sub('\+|\s|=', '', puzzle))}
    left_side, right_side = [i.strip() for i in puzzle.split('==')]
    left_side_elements = [(i.strip(), len(i.strip())) for i in left_side.split('+')]
    # Is there carryover?
    if max(i[1] for i in left_side_elements) < len(right_side):
        # If there is, since everything is single digit, the first letter of the right side = 1
        avaliable_letters[right_side[0]] = 1
    return avaliable_letters
