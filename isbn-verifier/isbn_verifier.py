from copy import copy
import re 
def is_valid(isbn: str) -> bool:
    isbn_copy = copy(isbn)
    isbn_copy = re.sub('-', '', isbn_copy)
    if not re.compile("^[0-9]{9}([0-9]|X)$").match(isbn_copy): #This matches a REGEX of how an ISBN should be with our ISBN. If it doesn't match, it's not valid!
        return False 
    isbn_list = list(isbn_copy)
    if isbn_list[9] == 'X':
            isbn_list[9] = 10
 
    #isbn_list = list(map(int, isbn_list)) This removes the int below. Should I?
 
    check_number = sum(int(couple[0]) * couple[1] for couple in zip(isbn_list, range(10, 0, -1)))
    
    return check_number % 11 == 0 if  check_number != 0 else False
    
