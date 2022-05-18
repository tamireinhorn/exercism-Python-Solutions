import re

PRESENTS = ['a Partridge in a Pear Tree', 'two Turtle Doves',
            'three French Hens',
            'four Calling Birds', 'five Gold Rings', 'six Geese-a-Laying',
            'seven Swans-a-Swimming',
            'eight Maids-a-Milking',
            'nine Ladies Dancing',
            'ten Lords-a-Leaping',
            'eleven Pipers Piping',
            'twelve Drummers Drumming']
DAYS = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh',
        'eighth', 'ninth',
        'tenth', 'eleventh', 'twelfth']


def recite(start_verse: int, end_verse: int) -> str:
    song_list = []
    for verse in range(start_verse, end_verse+1):
        beggining = (f"On the {DAYS[verse-1]} day of Christmas "
                     f"my true love gave to me: ")  # Format strings with variables
        song = beggining
        items = ', '.join(PRESENTS[verse-1::-1] or [PRESENTS[verse-1]])  # Empty lists are false, so if the slice returns empty 
        #Just use the sole item instead!
        if verse != 1:
            z = max([match.end() for match in re.finditer(',', items)])  # Get the position of the last comma
            items = f'{items[0:z]} and {items[z+1:]}.'
        else:
            items += '.'
        song += items
        song_list.append(song)
    return song_list
