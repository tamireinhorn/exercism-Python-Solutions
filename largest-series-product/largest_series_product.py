import functools


def largest_product(series: str, size: int):
    if size == 0:
        return 1
    if size < 0:
        raise ValueError("span must not be negative")
    if size > len(series):
        raise ValueError("span must be smaller than string length")
    try:
        int(series)
    except ValueError:
        raise ValueError("digits input must only contain digits")
    max_val = 0
    for i in range(0, len(series)):
        candidate = series[i:i+size]
        if len(candidate) == size:
            candidate_value = functools.reduce(lambda a, b: int(a) * int(b), candidate)
            if candidate_value >= max_val:
                max_val = candidate_value
    return max_val

