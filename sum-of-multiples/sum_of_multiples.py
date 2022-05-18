
def sum_of_multiples(limit, multiples):
    multiples_set = set()
    for multiple in multiples:
        if multiple != 0:
            quotient, rest = divmod(limit, multiple)
            if rest == 0:
                quotient -=1
            multiples_set = multiples_set.union(set(multiple * i for i in range(1,quotient+1)))
    return sum(multiples_set)
 