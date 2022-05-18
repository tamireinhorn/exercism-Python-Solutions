import re
from copy import copy


class PhoneNumber:
    def __init__(self, number):
        number = str(number)
        if re.search('[a-z]', number):
            raise ValueError('letters not permitted')
        if re.search('\:|@|!', number):
            raise ValueError('punctuations not permitted')
        number  = re.sub('\(|\)|\+|-|\s|\.|[a-z]', '', number)
        digits = len(number)
        try:
            n = int(number)
        except:
            raise ValueError('letters not permitted')
        if digits  == 11:
            if number[0] != '1':
                raise ValueError('11 digits must start with 1')
            else:
                number = number[1:]
        elif digits <= 9:
            raise ValueError('incorrect number of digits')
        elif digits > 11:
            raise ValueError('more than 11 digits')
        area_code = number[0:3]
        if area_code[0] == '0':
            raise ValueError('area code cannot start with zero')
        if area_code[0] == '1':
            raise ValueError('area code cannot start with one')
        exchange_code = number[3:6]
        if exchange_code[0] == '0':
            raise ValueError('exchange code cannot start with zero')
        if exchange_code[0] == '1':
            raise ValueError('exchange code cannot start with one')
        self.number = number 
        
        self.area_code = area_code
        self.exchange_code = exchange_code
        self.subscriber_code = number[6:]
    def pretty(self): 
        return "(" + self.area_code + ")-" + self.exchange_code + "-" + self.subscriber_code
