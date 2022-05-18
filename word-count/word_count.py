import re
from copy import copy

WORDS = re.compile('[a-z]+(?:\'[a-z]{1,2})?') #?: means a non capturing group, which emulates the ' + letters part of a contraction, and the ? after it makes it optional.

NUMBER = re.compile('[0-9]+')

def count_words(sentence):
    sentence = copy(sentence).lower()
    words = re.findall(WORDS, sentence)
    digits = re.findall(NUMBER, sentence)
    
    all_words = words + digits
    word_count = {}
    for word in all_words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count.setdefault(word, 1)
    return word_count


