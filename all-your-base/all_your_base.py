# Math based on :https://www.mathsisfun.com/base-conversion-method.html
def rebase(input_base: int, digits: list[int], output_base: int) -> list[int]:
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    number = 0
    for digit, power in zip(digits[::-1], range(len(digits))):
        if digit < 0 or digit >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
        number += digit * (input_base ** power)
    quotient, remainder = divmod(number, output_base)
    answer = [remainder]
    while quotient >= output_base:
        quotient, remainder = divmod(quotient, output_base)
        answer.append(remainder)
    if quotient != 0:
        answer.append(quotient)
    return answer[::-1]
