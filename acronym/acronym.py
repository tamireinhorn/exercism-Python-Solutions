def abbreviate(words):
    return "".join([word[0].upper() if word[0].isalpha() else '' for word in words.replace('_', '').replace('-', ' ').split()])
