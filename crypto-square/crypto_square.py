import math
import re


def cipher_text(plain_text: str) -> str:
    if plain_text:
        clean_text = re.sub('[^\w]', '' , plain_text.lower())
        message_length = len(clean_text)  # Normalize message. 
        r, c = calculate_rectangle(message_length)
        row_split = re.findall(f".{{1,{c}}}", clean_text)
        split_text = [chunk.ljust(c) for chunk in row_split]
        return ' '.join(''.join(column) for column in zip(*split_text))
    return ''

def calculate_rectangle(L: int) -> tuple:
    # - `r * c >= length(message)`,
    # - and `c >= r`,
    # - and `c - r <= 1`. # c, r are integers. Hence, either c = r OR c = r + 1
    # So either r = c = sqrt(L) or r is the closest integer to it.
    root = math.sqrt(L)
    if root % 1 == 0:
        c = int(root)
        r = c
    else:
        r = int(root)
        c = r + 1
    return r, c