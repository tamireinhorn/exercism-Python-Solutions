from itertools import chain


def can_chain(dominoes: list[tuple[int, int]]):
    # To verify chains, we need to have a base case (because this will likely be recursive)
    return _recursive_chain(dominoes)
    pass

def _recursive_chain(dominoes: list[tuple[int, int]]):
    if len(dominoes) == 0:
        return dominoes
    if len(dominoes) == 1:
        chainable = dominoes[0][0] == dominoes[0][1] # TODO, we could compare two dominoes, by looking at all 4 combinations and see if we can chain them.
        if chainable:
            return dominoes
        return 
    return 1