
EXPECTED_BAKE_TIME = 40


PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculate the bake time remaining.
    :param elapsed_bake_time: int baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers: int) -> int:
    """Calculate the time needed to prepare the lasagna.
    :param number_of_layers: int number of layers of the lasagna.
    :return: int number of minutes derived from 'PREPARATION_TIME'.

    Function that takes the number of layers that will be in the lasagna as an argument
    and returns how many minutes the lasagna will need to bake based on the 'PREPARATION_TIME'
    """

    return number_of_layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """Calculate the time needed to prepare the lasagna.
    :param number_of_layers: int number of layers of the lasagna.
    :return: int number of minutes derived from 'PREPARATION_TIME'.

    Function that takes the number of layers that will be in the lasagna as an argument
    and returns how many minutes the lasagna will need to bake based on the 'PREPARATION_TIME'
    """

    
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time