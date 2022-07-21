from __future__ import annotations
from copy import copy
from itertools import permutations


def can_chain(dominoes: list[tuple[int, int]]) -> list[tuple[int, int]] | None:
    if len(dominoes) == 0:
        return dominoes
    domino = dominoes[0]
    if len(dominoes) == 1:
        if domino[0] == domino[1]:
            return dominoes
        return
    sorted_dominoes = list(sorted(tuple(sorted(domino)) for domino in dominoes)) # If you sort your dominoes, then you don't need to worry about trying a previous piece again.
    # To make sure, try starting a chain with every domino
    for first_domino in sorted_dominoes:
        all_dominoes = copy(sorted_dominoes)
        chain = [first_domino]
        all_dominoes.remove(first_domino)
        # Then walk over every next domino and try to chain.
        for next_domino in all_dominoes:
            chain, chained = check_chainability(chain, next_domino)
            if not chained: # If we didn't even chain that domino, we KNOW this chain won't work because of sorting. So break the inner loop.
                break
        if validate_chain(chain, dominoes):
            return chain
    return  


def check_chainability(chain: list[tuple[int, int]], domino: tuple[int, int]) -> tuple[list[tuple[int, int]], bool]:
    """Function that gets a chain of dominoes and a domino and tries to add a new domino to the chain.

    Args:
        chain (list[tuple[int, int]]): The current chain of dominoes
        domino (tuple[int, int]): The domino we want to add to the chain

    Returns:
        tuple[list[tuple[int, int]], bool]: Returns the new chain and whether we were able to add the new domino to it.
    """
    # In a chain, you have two chaining points:
    chain_head = chain[0][0]
    chain_tail = chain[-1][-1]
    for possibilities in list(permutations(domino)):
        if possibilities[-1] == chain_head:
            return [possibilities] + chain, True
        if possibilities[0] == chain_tail:
            return chain + [possibilities], True
    return chain, False


def validate_chain(chain: list[tuple[int, int]], dominoes: list[tuple[int, int]]) -> bool:
    """Verifies if a chain is valid, having the same values for head and tail.

    Args:
        chain (list[tuple[int, int]]): The current chain of dominoes
        dominoes (list[tuple[int, int]]): The entire list of dominoes

    Returns:
        bool: True if the chain is valid, False if not.
    """
    chain_head = chain[0][0]
    chain_tail = chain[-1][-1]
    return chain_head == chain_tail and len(dominoes) == len(chain)