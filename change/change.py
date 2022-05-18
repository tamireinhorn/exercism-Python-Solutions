from itertools import combinations_with_replacement
## This solution is BRILLIANT but is based on a a community solution from RNeilsen, avaliable here: https://exercism.org/tracks/python/exercises/change/solutions/RNeilsen
def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("target can't be negative")
    # The core idea is that the biggest possible solution is just target // the smallest coin.
    max_coins = target // min(coins)
    # Also, the smallest possible solution is target // biggest coin.
    min_coins = target // max(coins)
    # To range over this, we just sum +1 
    for i in range(min_coins, max_coins + 1):
        # This is the bomb. This simply creates all possible combinations of size i from a list, with replacement (as the coins are infinite).
        combos = combinations_with_replacement(coins, i)
        # Now, you just loop over all possible combinations
        for combo in combos:
            # If the combo equals the target, we're done, just return it sorted as that's what the answer expects. Done.
            if sum(combo) == target:
                return sorted(combo)
    # If we never stop, the target is impossible.
    raise ValueError("can't make target with given coins")
