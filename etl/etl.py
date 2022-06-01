def transform(legacy_data):
    new_data = {}
    for score, letter_list in legacy_data.items():
        for letter in letter_list: 
             new_data[letter.lower()] = score 
    return new_data
