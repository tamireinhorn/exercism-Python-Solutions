"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""
from collections import Counter


def _yacht_score(dice):
    if len(set(dice)) == 1:
        return 50
    else:
        return DEFAULT_SCORE


def _singles_score(dice, category):
    c = Counter(dice)
    return category * c.get(category, 0)


def _full_house_score(dice):
    c = Counter(dice)
    c_values = c.values()
    if 2 in c_values and 3 in c_values:
        return sum(dice)
    else:
        return DEFAULT_SCORE


def _four_of_a_kind_score(dice):
    c = Counter(dice)
    c_values = c.values()
    if 4 in c_values or 5 in c_values:
        for item in c:
            value = c[item]
            if value >= 4:
                return 4 * item
    else:
        return DEFAULT_SCORE


def _little_straight_score(dice):
    dice.sort()
    if dice == list(range(1, 6)):
        return 30
    else:
        return DEFAULT_SCORE


def _big_straight_score(dice):
    dice.sort()
    if dice == list(range(2, 7)):
        return 30
    else:
        return DEFAULT_SCORE


def _choice_score(dice):
    return sum(dice)


def score(dice, category):
    try:
        return category(dice)
    except:
        raise ValueError('There is no such category')


YACHT = _yacht_score
ONES = lambda dice: _singles_score(dice, 1)
TWOS = lambda dice: _singles_score(dice, 2)
THREES = lambda dice: _singles_score(dice, 3)
FOURS = lambda dice: _singles_score(dice, 4)
FIVES = lambda dice: _singles_score(dice, 5)
SIXES = lambda dice: _singles_score(dice, 6)
FULL_HOUSE = _full_house_score
FOUR_OF_A_KIND = _four_of_a_kind_score
LITTLE_STRAIGHT = _little_straight_score
BIG_STRAIGHT = _big_straight_score
CHOICE = _choice_score
DEFAULT_SCORE = 0
