import string, re
def is_pangram(sentence):
    return set(re.findall('[a-z]', sentence.lower())) == set(string.ascii_lowercase)