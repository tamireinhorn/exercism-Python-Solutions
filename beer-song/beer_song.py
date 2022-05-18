from itertools import chain

def format_verse(start):
    s_var = lambda x: int(x != 1) * 's'
    next_bottles = lambda bottles: bottles -1 if bottles - 1 > 0 else 'no more'
    current_bottles = lambda bottles: bottles if bottles != 0 else 'no more'
    next_bottles = next_bottles(start)
    bottles = current_bottles(start)
    s, next_s = s_var(bottles),  s_var(next_bottles)
    first_verse = f"{bottles} bottle{s} of beer on the wall, {bottles} bottle{s} of beer.".capitalize()
    last_verse = f"Take {'it' if next_bottles == 'no more' else 'one'} down and pass it around, {next_bottles} bottle{next_s} of beer on the wall."
    if bottles == 'no more':
        last_verse = "Go to the store and buy some more, 99 bottles of beer on the wall."
    return [first_verse, last_verse]


def recite(start, take = 1):
    answer = []
    while take > 0:
        answer.append(format_verse(start))
        if take != 1:
            answer.append([""])
        start -=1
        take -=1
    return list(chain.from_iterable(answer))

