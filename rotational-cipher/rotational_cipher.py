
import string 
alphabet = string.ascii_lowercase
def rotate(text, key):
    modified_alphabet = alphabet[key:] + alphabet[:key]
    answer = ''.join([substitute(letter, modified_alphabet) for letter in text])
    return answer


def substitute(character: string, modif_alphabet):
    if character.isalpha():
        if character == character.upper():
            return modif_alphabet[alphabet.index(character.lower())].upper()
        else:
            return modif_alphabet[alphabet.index(character.lower())]
    return character
        