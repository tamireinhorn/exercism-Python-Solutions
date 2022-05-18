from collections import namedtuple



def best(min_factor, max_factor, largest):
    if largest:
        start = max_factor
        end = min_factor-1
        step = -1
        func = lambda x: x
    else:
        start = min_factor
        end = max_factor+1
        step = 1
        func = lambda x: -x 
    if max_factor < min_factor:
        raise ValueError("min must be <= max")
    Palindrome = namedtuple('Palindrome', 'number factors')
    PalindromeList = []
    #Use two pointers in the range:
    # [1,2,3,4,5,6,7,8,9] 
    # First pointer is at 1, and then we start the second pointer at the same place, but we walk it all over the list.
    # 
    for first_pointer in range(start, end, step):
        for i in range(first_pointer, end, step):
            mult = first_pointer * i 
            if func(mult) < max((func(i.number) for i in PalindromeList), default=func(mult)):
                break
            if str(mult) == str(mult)[::-1]:
                PalindromeList.append(Palindrome(mult, [first_pointer, i]))
                break    
    max_palindrome = None
    if PalindromeList:
        max_palindrome = abs(max(func(i.number) for i in PalindromeList))
    factors = []
    temp = (i.factors for i in PalindromeList if i.number == max_palindrome)
    list(map(factors.append, temp))
    return max_palindrome, factors



def largest(min_factor, max_factor):
    """Given a range of numbers, find the largest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    return best(min_factor, max_factor, 1)


def smallest(min_factor, max_factor):
    
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    return best(min_factor, max_factor, 0)
    