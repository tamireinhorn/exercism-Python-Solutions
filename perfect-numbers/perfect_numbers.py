def aliquot_sum(number):
    return sum(i for i in range(1, number) if number % i == 0)


def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    aliquot = aliquot_sum(number)
    if aliquot == number:
        return "perfect"
    if aliquot > number:
        return "abundant"
    return "deficient"
