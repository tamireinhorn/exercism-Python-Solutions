from re import S


def steps(number):
#     Take any positive integer n. If n is even, divide n by 2 to get n / 2. If n is
# odd, multiply n by 3 and add 1 to get 3n + 1. Repeat the process indefinitely.
# The conjecture states that no matter which number you start with, you will
# always reach 1 eventually.
    number_of_steps = 0
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    while number != 1:
        quotient, remainder = divmod(number, 2)
        if remainder == 0:
            number = quotient
        else:
            number = (3 * number) + 1
        number_of_steps +=1 
    return number_of_steps

 