def is_armstrong_number(number):
    number_string = str(number)
    digits = len(number_string)
    if digits == 1:
        return True
    else:
        armstrong = sum([int(digit) ** digits for digit in number_string])
        return number == armstrong
    