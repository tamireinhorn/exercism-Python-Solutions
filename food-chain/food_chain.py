BASIS = "I know an old lady who swallowed a"
END =  "I don't know why she swallowed the fly. Perhaps she'll die."
ANIMALS = ["fly", "spider", "bird", "cat", "dog", "goat", "cow", "horse"]
SPIDER_EXTRA = "wriggled and jiggled and tickled inside her"
ADDENDUM = ["", f"It {SPIDER_EXTRA}.", "How absurd to swallow a bird!", 
            "Imagine that, to swallow a cat!", "What a hog, to swallow a dog!", "Just opened her throat and swallowed a goat!",
             "I don't know how she swallowed a cow!", "She's dead, of course!"]
 
def generate_verse(verse_number: int):
    verse_animal = ANIMALS[verse_number-1]
    verse = [f"{BASIS} {verse_animal}."]
    if verse_number > 1:
        verse.append(ADDENDUM[verse_number-1])
        if verse_number < 8:
            reverse_animals = ANIMALS[:verse_number][::-1]
            short_reverse_animals = reverse_animals[1:]
            for animal, next_animal in zip(reverse_animals, short_reverse_animals):
                if next_animal == 'spider':
                    next_animal = f"{next_animal} that {SPIDER_EXTRA}"
                verse.append(f"She swallowed the {animal} to catch the {next_animal}.")
            verse.append(END)
    if verse_number == 1:
        verse.append(END)
    return verse 


def recite(start_verse, end_verse):
    full_verse = []
    for verse_number in range(start_verse, end_verse+1):
        full_verse += generate_verse(verse_number)
        if start_verse != end_verse and verse_number < end_verse:
            full_verse.append("")
    return full_verse
