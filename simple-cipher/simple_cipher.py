import string, itertools
from secrets import randbelow
alphabet = list(string.ascii_lowercase)
class Cipher:
    def __init__(self, key=None):
        if not key:
            key = ''.join([alphabet[randbelow(len(alphabet))] for i in range(100)])
        self.key = key

    def encode(self, text):
        key = self.key
        message = ''
        for letter, new_index in zip(text, itertools.cycle(key)):
            modified_alphabet = alphabet[alphabet.index(new_index):] + alphabet[:alphabet.index(new_index)]
            message += modified_alphabet[alphabet.index(letter)]
        return message
            
    def decode(self, text):
        key = self.key
        message = ''
        for letter, new_index in zip(text, itertools.cycle(key)):
            modified_alphabet = alphabet[alphabet.index(new_index):] + alphabet[:alphabet.index(new_index)]
            message += alphabet[modified_alphabet.index(letter)]
        return message
            
        
