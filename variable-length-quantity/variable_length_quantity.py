def encode(numbers: list[int]):
    answer = []
    for number in numbers:
        answer += encode_number(number)
    return answer


def decode(bytes_):
    answer = ""
    # In VLQ, the last bit is a continuation byte. If it's set but there is nothing after it, the sequence is incomplete:
    binary_reprs = [bin(byte)[2:].rjust(8, '0') for byte in bytes_]

    if binary_reprs[-1][0] == '1': # With eight, the byte has the continuation bit put. And the last one CAN'T be 1.
        raise ValueError("incomplete sequence")
    for byte in bytes_:
        answer += bin(byte | 128)[3:] # Convert to binary with an OR due to base-128, then remove the prefix.
    for bin_rep in binary_reprs:
        # Remember the split you did, imbecile, then do the opposite.
        pass
    return [int(answer, 2)] # Then reconvert to base 2 as int and put it as a list.


def encode_number(number: int):
    if number == 0:
        return [0]
    binary_rep = bin(number)[2:] # Get binary string but strip it of the part we don't need.
    base_128 = [binary_rep[::-1][i:i+7][::-1].rjust(7, '0') for i in range(0, len(binary_rep), 7)][::-1] # Break in group of 7 bits from the rightmost bit.
    for index, element in enumerate(base_128[:len(base_128) - 1]):
        base_128[index] = f'1{element[0:]}' # MSB is the leftmost bit and it should be 1 for all elements but the last, since it means there is another byte to the right.
    base_128[0] = f'0{base_128[0][0:]}'
    return [int(b, 2) for b in base_128]
