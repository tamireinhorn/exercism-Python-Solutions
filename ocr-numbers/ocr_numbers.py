import enum


def convert(input_grid):
    input_size, remainder = divmod(len(input_grid[0]), 3)
    number_list = []
    for index, _ in enumerate(input_size):
        beg_index = index
        end_index = index + 3
        number = [input_grid[0][0:3], input_grid[1][0:3], input_grid[2][0:3], input_grid[3][0:3]]
        number_list.append(number)
    return recognize_number(input_grid)

ZERO = [" _ ", "| |", "|_|", "   "]
ONE = ["   ", "  |", "  |", "   "]
TWO = [" _ ", " _|", "|_ ", "   "]
THREE = [" _ ", " _|", " _|", "   "]
FOUR = ["   ", "|_|", "  |", "   "]
FIVE = [" _ ", "|_ ", " _|", "   "]
SIX = [" _ ", "|_ ", "|_|", "   "]
SEVEN = [" _ ", "  |", "  |", "   "]
EIGHT = [" _ ", "|_|", "|_|", "   "]
NINE = [" _ ", "|_|", " _|", "   "]

NUMBERS_DICT = {tuple(ZERO): '0', tuple(ONE): '1', tuple(TWO): '2',
                tuple(THREE): '3', tuple(FOUR): '4', tuple(FIVE): '5',
                tuple(SIX): '6', tuple(SEVEN): '7', tuple(EIGHT): '8', tuple(NINE): '9'}

def recognize_number(grid):
    return NUMBERS_DICT.get(tuple(grid), '?')
# My solution idea is to separate in grids of 3x4, match them to numbers, so we would have like 2 functions. 



