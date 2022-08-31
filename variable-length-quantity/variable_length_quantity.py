def encode(numbers):
    #Another way to look at this is to represent the value in base-128 and then set the MSB of all but the last base-128 digit to 1.
    pass

def decode(bytes_):
    answer = ""
    # In VLQ, the last bit is a continuation byte. If it's set, the sequence is incomplete:
    if bytes_[-1] >> 7 == 1:
        raise ValueError("incomplete sequence")
    for byte in bytes_:
        answer += bin(byte | 128)[3:] # Convert to binary with an OR due to base-128, then remove the prefix.
    return [int(answer, 2)] # Then reconvert to base 2 as int and put it as a list.
