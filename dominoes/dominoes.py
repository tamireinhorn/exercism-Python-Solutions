from itertools import permutations

def can_chain(dominoes: list[tuple[int, int]]):
    # To verify chains, we need to have a base case (because this will likely be recursive)
    return _recursive_chain(dominoes)
    pass

def _recursive_chain(dominoes: list[tuple[int, int]]):
    if len(dominoes) == 0:
        return dominoes
    if len(dominoes) == 1:
        return check_chainability(dominoes[0], dominoes[0])
    return 1


def check_chainability(domino_1: tuple[int, int], domino_2: tuple[int, int]):
    if domino_1 == domino_2:
        if domino_1[0] == domino_1[1]:
            return [domino_1]
        return None
    for domino_1_possibility in list(permutations(domino_1)):
        for domino_2_possibility in list(permutations(domino_2)):
            if domino_1_possibility[0] == domino_2_possibility[0]:
                if domino_1 == domino_2:
                    return [domino_1]
                return [domino_1_possibility, domino_2_possibility]