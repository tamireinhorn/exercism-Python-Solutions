ALLERGIES_SCORE = ['eggs', 'peanuts', 'shellfish', 'strawberries',
                   'tomatoes', 'chocolate', 'pollen', 'cats']

class Allergies:

    def __init__(self, score: int):
        self.score = score
        self.lst = self.list_of_allergies()
     
    def allergic_to(self, item: str) -> bool:
        return item in self.lst

    def list_of_allergies(self) -> list[str]:
        score = self.score
        mask = 1 # This mask starts as 0b1, which stands for eggs.
        # The idea is if we do a bitwise AND (&) with a score of, for example, 3, which is 0b11.
        # This will return 0b01, which would be True, that is, you are allergic to eggs.
        allergy_list = []
        for allergen in ALLERGIES_SCORE:
            if score & mask: # Bitwise AND can be done in ints!
                allergy_list.append(allergen)
            # Shift the bit on the mask to the left for the next allergen
            mask <<= 1
        return allergy_list
