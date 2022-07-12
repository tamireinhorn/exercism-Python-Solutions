BASIS = "I know an old lady who swallowed a"
END =  "I don't know why she swallowed the fly. Perhaps she'll die."
ANIMALS = ["fly", "spider"]
ADDENDUM = ["", "It wriggled and jiggled and tickled inside her.", "How absurd to swallow a bird!"]


def generate_verse(verse_number: int):
    verse = [f"{BASIS} {ANIMALS[verse_number-1]}."]
    if verse_number > 1:
        verse.append(ADDENDUM[verse_number-1])
    verse.append(END)
    return verse 


def recite(start_verse, end_verse):
    return generate_verse(start_verse)
