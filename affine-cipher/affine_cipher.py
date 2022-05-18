
from string import ascii_lowercase
import re
from math import gcd
ALPHABET = ascii_lowercase


def encrypt_letter(letter, a, b, m):
    return (a * ALPHABET.index(letter) + b) % m


def clean(a):
    m = len(ALPHABET)
    if not gcd(a, m) == 1:
        raise ValueError('a and m must be coprime.')
    return m

def encode(plain_text, a, b):
    m = clean(a)
    clean_text = re.sub('[^0-9a-zA-Z]+', '', plain_text.lower()) 
    answer = ''
    counter = 1
    for letter in clean_text: 
        if str.isalpha(letter):
            next_letter = ALPHABET[encrypt_letter(letter, a, b, m)]
        else:
            next_letter = letter
        if counter > 5:
            counter = 1
            next_letter = f' {next_letter}'
        counter +=1 
        answer += next_letter
    return answer


def decrypt_letter(letter, a, b, m):
    return pow(a, -1, m) * (ALPHABET.index(letter) - b) % m 


def decode(ciphered_text, a, b):
    m = clean(a)
    clean_text = re.sub(' ', '', ciphered_text)
    ans = ''.join(ALPHABET[decrypt_letter(letter, a, b, m)] if str.isalpha(letter) else letter for letter in clean_text)
    return ans