import re 

OPERATIONS = re.compile('plus|minus|divided|multiplied')


def answer(question):
    digits = list(map(int, re.findall('-?\d+', question)))
    number_of_digits = len(digits)
    if number_of_digits == 0 and re.search('is\?', question):
        raise ValueError("syntax error")
    if number_of_digits == 0:
        raise ValueError("unknown operation")
    answer = digits[0]
    if re.search('is \d\?', question):
        return answer
    if re.search('\d\s\d', question):
        raise ValueError("syntax error")
    found_operations = re.findall(OPERATIONS, question)
    number_of_operations = len(found_operations)
    if number_of_operations == 0 and number_of_digits == 1:
        raise ValueError("unknown operation")
    if number_of_digits != number_of_operations + 1:
        raise ValueError('syntax error')
    if number_of_operations == number_of_digits and number_of_digits == 0:
        raise ValueError('syntax error')
    for digit, operation in zip(digits[1:], found_operations):
        x, y = digit, operation
        if operation == 'plus':
            answer += digit
        elif operation == 'minus':
            answer -= digit
        elif operation == 'divided':
            answer = answer / digit
        elif operation == 'multiplied':
            answer = answer * digit
    return answer
