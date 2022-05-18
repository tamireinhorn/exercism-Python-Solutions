def get_rounds(number):
    """

     :param number: int - current round number.
     :return: list - current round and the two that follow.
    """

    return [number + i for i in range(3)]


def concatenate_rounds(rounds_1, rounds_2):
    """

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return:  bool - was the round played?
    """

    return number in rounds


def card_average(hand):
    """

    :param hand: list - cards in hand.
    :return:  float - average value of the cards in the hand.
    """

    return sum(hand) / len(hand)


def approx_average_is_average(hand):
    """

    :param hand: list - cards in hand.
    :return: bool - is approximate average the same as true average?
    """
    median = hand[len(hand)//2]
    approx_average = (hand[0] + hand[-1])/2
    avg = card_average(hand)
    return median == avg or approx_average == avg


def average_even_is_average_odd(hand):
    """

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    even = 0
    odd = 0 
    even_count = 0 
    odd_count = 0 
    for index, element in enumerate(hand):
        if index % 2 == 0:
            even += element
            even_count +=1
        else:
            odd += element
            odd_count += 1
    
        
    even_avg = even / even_count
    odd_avg = odd / odd_count
        
    return even_avg == odd_avg


def maybe_double_last(hand):
    """

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    if hand[-1] == 11:
        hand[-1] = 22
    return hand 
