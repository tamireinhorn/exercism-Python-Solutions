def rebase(input_base: int, digits: list[int], output_base: int) -> list[int]:
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    number = sum(digit * (input_base ** power) for digit, power in zip(digits[::-1], range(len(digits))))
    quotient, remainder = divmod(number, output_base)
    answer = [remainder]
    while quotient > output_base:
        quotient, remainder = divmod(quotient, output_base)
        print(2)
    answer.append(quotient)
    return answer[::-1]
