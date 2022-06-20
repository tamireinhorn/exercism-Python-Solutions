import re
from itertools import permutations

def solve(puzzle: str):
    elements = re.findall('\w+', puzzle) # Splits the puzzle into all of the elements of the equation.
    first_letters = set(w[0] for w in elements) # We need to know the first letters, just so we never have them = 0 because 0 leading is forbidden.
    avaliable_letters = set(''.join(elements)) # We also need to know all possible letters.
    number_of_letters = len(avaliable_letters)
    if number_of_letters > 10:
        return ValueError('Too many different letters, only 10 allowed.')
    for permutation in permutations(range(10), number_of_letters): # We create all possible combinations of values the letters can have.
        invalid_permutation = False # We can't have 0 leading digit, so we need to check
        avaliable_letters_dict = {letter: value for letter, value in zip(avaliable_letters, permutation)}
        for first_letter in first_letters: # If any of the first letters has a value of 0 in the dict.
            if avaliable_letters_dict[first_letter] == 0:
                invalid_permutation = True # This is permutation doesn't work, we can skip ahead.
                break 
        if not invalid_permutation:
            new_puzzle = translate(puzzle, avaliable_letters_dict)
            if eval(new_puzzle): # If the equation produced is true, we've found a solution and can just return it.
                return avaliable_letters_dict 
    return None

def translate(string: str, dictionary: dict[str, any]) -> str:
    """Helper function to replace characters in a string with their value in a dictionary mapping.

    Args:
        string (str): String to be translated.
        dictionary (dict[str, any]): Dictionary containing the mapping between letters and their values
    Returns:
        new_string (str): String with new values.
    """
    new_string = string
    for key, value in dictionary.items():
        new_string = new_string.replace(key, str(value))
    return new_string