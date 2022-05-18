from string import ascii_lowercase
import re

ALPHABET = ascii_lowercase
CIPHER = ALPHABET[::-1]


def encode(plain_text):
    answer = ''
    counter = 1
    clean_text = re.sub('[^0-9a-zA-Z]+', '', plain_text.lower()) 
    for letter in clean_text:
        next_letter = ''
        x = re.search(letter, ALPHABET)
        if x:
            index = x.start()
            next_letter = CIPHER[index]
        else:
            next_letter = letter
        if counter > 5:
            next_letter =  f' {next_letter}'
            counter = 1
        answer += next_letter
        counter += 1
    return answer


def decode(ciphered_text):
    answer = ''
    clean_text = re.sub('[^0-9a-zA-Z]+', '', ciphered_text)
    for letter in clean_text:
        x = re.search(letter, CIPHER)
        if x: 
            index = x.start()
            next_letter = ALPHABET[index]
        else:
            next_letter = letter 
        answer += next_letter
    return answer 