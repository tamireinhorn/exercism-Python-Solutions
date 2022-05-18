from collections import Counter 
def find_anagrams(word, candidates):
    results = []
    lower_word = word.lower()
    for possibility in candidates:
        possibility_lower = possibility.lower()
        if Counter(possibility_lower) == Counter(lower_word) and possibility_lower != lower_word:
            results.append(possibility)
    return results 