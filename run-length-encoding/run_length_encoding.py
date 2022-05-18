import re


def decode(string):
    patterns = re.findall("(\d*)([A-Z]|\s)", string, flags= re.IGNORECASE)
    default_if_empty = lambda x: 1 if x == '' else int(x)
    return ''.join([default_if_empty(z[0]) * z[1] for z in patterns])


def encode(string): 
    answer = ""
    accumulated = 0
    while accumulated < len(string):
        current_letter = string[accumulated]
        current_match = re.search(f"({current_letter})+", string[accumulated:])
        size = current_match.end() - current_match.start()
        accumulated+= size
        answer += f"{size}{current_letter}" if size > 1 else f"{current_letter}"
    return answer
