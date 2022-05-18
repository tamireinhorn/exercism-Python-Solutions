def square(number):
    if number <= 0 or number > 64:
        raise ValueError('square must be between 1 and 64')
    return 2 ** (number - 1)

def total():
    return sum([square(number) for number in range(1,65)])