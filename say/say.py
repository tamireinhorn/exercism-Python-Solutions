import textwrap

NUMBER_DICT = {"0": "zero", "1": "one", "2": "two",
               "3": "three", "4": "four", "5": "five",
               "6": "six", "7": "seven", "8": "eight",
               "9": "nine", "10": "ten", "11": "eleven",
               "12": "twelve", "13": "thirteen",
               "15": "fifteen", "20": "twenty", "30": "thirty",
               "40": "forty", "50": "fifty","60": "sixty",
               "70": "seventy", "80": "eighty", "90": "ninety",
               "00": "zero"
               }

suffixes = ["", " thousand", " million", " billion"]


def say(number: int) -> str:
    if number < 0 or number > 999999999999:
        raise ValueError("input out of range")
    # Stringify
    number_string = str(number)[::-1]
    # Simple numbers are solvable directly!
    if len(number_string) <= 3:
        return chunk_solver(str(number))
    # Split it into chunks of 3:
    reverse = lambda x: x[::-1]
    chunks = textwrap.wrap(number_string, 3)
    # The chunks need to be correctly oriented.
    chunks = list(map(reverse, chunks))
    answer = []
    for chunk, suffix in zip(chunks, suffixes):
        result = chunk_solver(chunk)
        if result:
            answer.append(f"{result}{suffix}")
    return ' '.join(reverse(answer)).strip()


def zero_cleaner(part):
    return "" if "zero" in part else part


def chunk_solver(chunk):
    if chunk in NUMBER_DICT:
        return NUMBER_DICT.get(chunk)
    # Padding makes the code MUCH more simple.
    chunk = f"{'0' * (3 - len(chunk))}{chunk}"
    #The first digit is always the hundred one:
    first_digit = zero_cleaner(NUMBER_DICT.get(chunk[0]) + " hundred")
    #The rest SHOULD Be evaluated together
    if chunk[1:] in NUMBER_DICT:
        second_part = zero_cleaner(NUMBER_DICT.get(chunk[1:]))
    else:
        if chunk[1] == "1":
            second_part = NUMBER_DICT.get(chunk[2]) + "teen"
        else:
            second_part_decimal = zero_cleaner(NUMBER_DICT.get(f"{chunk[1]}0"))
            hifen = "-" if second_part_decimal else ""
            second_part = second_part_decimal + zero_cleaner(f"{hifen}{NUMBER_DICT.get(chunk[2])}")
    return f"{first_digit} {second_part}".strip()



