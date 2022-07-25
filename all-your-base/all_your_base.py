from math import remainder
def rebase(input_base: int, digits: list[int], output_base: int) -> list[int]:
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    # What is the output base in terms of the input base


        # (4 \* 10^1) + (2 \* 10^0)
        # (2^2 + 0 * 2^1 + 0 * (2^0)) * (2^3 + 2^0) 
            # 10 = 2 ^ 3 + 2 
            # 4  * (2 ^3 + 2^0)
            # 2^5 + 2^3
        # The number 101010, *in base 2*, means:

        # (1 \* 2^5) + (0 \* 2^4) + (1 \* 2^3) + (0 \* 2^2) + (1 \* 2^1) + (0 \* 2^0)
    convert_number_to_base(input_base, output_base)
    pass

def convert_number_to_base(input_base: int, output_base: int):
    power = 0
    # I want to write the output base in terms of input;
    # So 10 should become 2^3 + 2^0
    # If I were to write 40 in base 3
    # 3^3 = 27, so we have 13 more.
    # 3^3 + 
    number = input_base ** power
    while number < output_base:
        number = input_base ** power
        power += 1
    if number > output_base:
        power -= 1
    print(power)