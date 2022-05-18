VERSES = ["house that Jack built", "malt that lay in", "rat that ate", "cat that killed",
            "dog that worried", "cow with the crumpled horn that tossed", "maiden all forlorn that milked", 
            "man all tattered and torn that kissed", "priest all shaven and shorn that married",
            "rooster that crowed in the morn that woke", "farmer sowing his corn that kept","horse and the hound and the horn that belonged to"]
BEGINNING = "This is"
THE = "the"


def create_poem():
    poem = []
    for i in range(len(VERSES)):
        verse = [f"{THE} {VERSES[j]}" for j in range(i,-1, -1)] 
        verse = f"{BEGINNING} {' '.join(verse)}."
        poem.append(verse)
    return poem


def recite(start_verse, end_verse):
    poem = create_poem()
    return  poem[start_verse-1:end_verse]
