from copy import copy
import re 

VOWELS = ['a', 'e', 'i', 'o', 'u']
VOWEL_SOUNDS = VOWELS + ['xr', 'yt']

PIG_LATIN_SUFFIX = 'ay'


def translate(text):
    return ' '.join(list(map(translate_word, text.split())))

    
def translate_word(word):
    answer = copy(word).lower()
    VOWELS_string = '|'.join(VOWEL_SOUNDS)
    if re.match('[a-z]y', answer): # This is to match two letter words with y, Rule 4.
        return answer[::-1] + PIG_LATIN_SUFFIX
    elif re.match(VOWELS_string, answer): # This is to match vowels, for Rule 1
         return answer + PIG_LATIN_SUFFIX
    elif re.match(f'[^{VOWELS_string}]+qu', answer): #This is to match consonant cluster + qu, Rule 3
        qu_position = re.search('qu', answer).end()
        return answer[qu_position:] + answer[:qu_position] + PIG_LATIN_SUFFIX
    elif re.match(f'qu', answer): # This is to match just qu
        return answer[2:] + answer[:2] + PIG_LATIN_SUFFIX
    else:
        next_vowel = re.search(f'[{VOWELS_string}|y](?!xr)]',answer[1:]).start() +1 # Gets the next vowel, but excludes xr! and counts y as vowel.
        return answer[next_vowel:] + answer[:next_vowel] + PIG_LATIN_SUFFIX
        

        
        

            
       
            
            
    
