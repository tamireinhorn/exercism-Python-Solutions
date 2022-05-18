from collections import Counter
from enum import IntEnum, unique

# Instead of using a dict as a data structure, I decided to use an actual enum!
# IntEnum regularly accepts multiple names for a same value, and the @unique decorator stops that from happening!
@unique
class Score(IntEnum):
    """Score of a poker hand. Higher values beat lower values."""
    high_card = 1
    pair = 2
    two_pairs = 3
    three_of_a_kind = 4
    straight = 5
    flush = 6
    full_house = 7
    four_of_a_kind = 8
    straight_flush = 9


def parse_card(card: str) -> tuple: 
    """Separates the card into value and suit.

    Args:
        card (str): String representing a poker card, in the format ValueSuit, like '9D' (9 of Diamonds).

    Returns:
        tuple: Returns a tuple of the card, like (Value, Suit). Ex: '9D' -> ('9', 'D').
    """
    if len(card) == 3:
        #If we receive a card whose len is 3, this is 10 + S(suit), so we replace 10 for T to make things easier.
        return 'T', card[2]
    else:
        return card[0], card[1]



def canonical(hand):
    """Return the canonical form of the poker hand as a pair (q, r) where
    q is a value from the Score enumeration, and r is a list of the
    distinct card ranks in the hand (from 1=low ace to 14=high ace),
    ordered in descreasing order by frequency and then by rank. These
    canonical forms can be compared to see who wins. The hand must be
    a sequence of five cards given as two-character strings in the
    form 2H, TS, JC etc.

    >>> canonical('TD 7H KH TS 7S'.split()) # two pairs (tens and sevens)
    (<Score.two_pairs: 3>, [10, 7, 13])
    >>> canonical('3C AH 4D 2S 5C'.split()) # ace-low straight
    (<Score.straight: 5>, [5, 4, 3, 2, 1])
    >>> canonical('JH 2H JC JS 2D'.split()) # full house (twos and jacks)
    (<Score.full_house: 7>, [11, 2])
    >>> canonical('TS 4S 8S QS 5S'.split()) # queen-high flush
    (<Score.flush: 6>, [12, 10, 8, 5, 4])

    """
    # This just iterates over the parsed hand, and gets the distinct suits. One suit only = Flush.
    flush = len(set(suit for _, suit in hand)) == 1
    # for rank, _ in hand gets the value of the card, and compares it to the position in the string.
    # This string is built in such a way that 2 has a value of 2 and so on. 
    # This therefore will return to us the value of each card, and sort it.
    ranks = sorted('--23456789TJQKA'.find(rank) for rank, _ in hand)
    # There is one specific straight that is just A,2,3,4,5, and whose rankings will be sorted as 2,3,4,5,14
    # So we just manually put that Ace as a '1', which would never happen, thus making it the lowest straight. 
    if ranks == [2, 3, 4, 5, 14]: 
        ranks = [1, 2, 3, 4, 5]
    # In all other cases, a straight is just a sequence of values from the first card's value to it + 5!
    straight = ranks == list(range(ranks[0], ranks[0] + 5))
    # This just counts the values of the cards to search for pairs and the like.
    count = Counter(ranks)
    counts = sorted(count.values())
    distinct_ranks = sorted(count, reverse=True, key=lambda v:(count[v], v))
    if flush and straight:       q = Score.straight_flush
    elif counts == [1, 4]:       q = Score.four_of_a_kind
    elif counts == [2, 3]:       q = Score.full_house
    elif flush:                  q = Score.flush
    elif straight:               q = Score.straight
    elif counts == [1, 1, 3]:    q = Score.three_of_a_kind
    elif counts == [1, 2, 2]:    q = Score.two_pairs
    elif counts == [1, 1, 1, 2]: q = Score.pair
    else:                        q = Score.high_card
    return q, distinct_ranks


def best_hands(hands):
    parsed_cards = list(list(map(parse_card, hand.split())) for hand in hands)
    ranked_hands = list(map(canonical, parsed_cards))
    best_hand = max(ranked_hands)
    return [hands[index] for index, score in enumerate(ranked_hands) if score == best_hand]