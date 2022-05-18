def slices(series, length):
    if length < 0:
        raise ValueError("slice length cannot be negative")
    if length == 0:
        raise ValueError("slice length cannot be zero")
    if not series:
        raise ValueError("series cannot be empty")
    series_size = len(series)
    if series_size < length:
        raise ValueError("slice length cannot be greater than series length")
    max_iteration = series_size - length +1
    sequences = []
    i = 0
    while i + length -1 < series_size:
        sequences.append(series[i:i+length])
        i+=1
 
    return sequences

