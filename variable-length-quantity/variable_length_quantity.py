def encode(numbers: list[int]):
    answer = []
    for number in numbers:
        answer += encode_number(number)
    return answer


def decode(bytes_):
    answer = ""
    # In VLQ, the last bit is a continuation byte. If it's set but there is nothing after it, the sequence is incomplete:
    binary_reprs = [bin(byte)[2:] for byte in bytes_]

    if binary_reprs[-1][0] == '1' and len(binary_reprs[-1]) == 8: # With eight, the byte has the continuation bit put. And the last one CAN'T be 1.
        raise ValueError("incomplete sequence")
    # for byte in bytes_:

    result = []
    current_result = 0
    for byte, binar in zip(bytes_, binary_reprs):
        current_result = (current_result << 7) | (byte & 0b1111111)
        if binar.rjust(8, '0')[0] == '0':
            result.append(current_result)
            current_result = 0
    return result


def encode_number(number: int):
    if number == 0:
        return [0]
    binary_rep = bin(number)[2:] # Get binary string but strip it of the part we don't need.
    # Get the rightmost bit (hence invert once), get a group of 7 (i:i+7), and then desinvert it so you have it in the original orinetation.
    # That is the number in the base 128 format.
    base_128 = [binary_rep[::-1][i:i+7][::-1].rjust(7, '0') for i in range(0, len(binary_rep), 7)][::-1]
    for index, element in enumerate(base_128[:len(base_128) - 1]):
        # MSB is the leftmost bit and it should be 1 for all elements but the last, since it means there is another byte to the right.
        base_128[index] = f'1{element[0:]}'
    base_128[0] = f'0{base_128[0][0:]}'
    return [int(b, 2) for b in base_128]
