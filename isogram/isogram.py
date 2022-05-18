from collections import Counter
import re 


def is_isogram(string):
    clean_string = string.lower()
    clean_string = re.sub('-|\s', '', clean_string)
    c = Counter(clean_string)
    return all(x == 1 for x in c.values())
