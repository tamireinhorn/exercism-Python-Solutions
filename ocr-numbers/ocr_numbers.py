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

# Break down a grid into grids of 4 lines, then process them as 4x3 of numbers
def regular_grid(input_grid: list[str]) -> str:
    input_size, remainder = divmod(len(input_grid[0]), 3)
    if remainder > 0:
        raise ValueError("Number of input columns is not a multiple of three")
    answer = ""
    for index in range(input_size):
        beg_index = index * 3 
        end_index = beg_index + 3
        number = [input_grid[0][beg_index:end_index], 
                input_grid[1][beg_index:end_index], 
                input_grid[2][beg_index:end_index], 
                input_grid[3][beg_index:end_index]]
        answer += NUMBERS_DICT.get(tuple(number), '?')
    return answer


def convert(grid: list[str]) -> str:
    answer = []
    lines, remainder = divmod(len(grid), 4)
    if remainder > 0:
        raise ValueError("Number of input lines is not a multiple of four")           
    for index in range(lines):
        beg = index * 4
        end = beg + 4
        answer.append(regular_grid(grid[beg:end]))
    return ','.join(answer)
