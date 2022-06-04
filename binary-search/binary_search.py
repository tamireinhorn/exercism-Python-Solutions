def find(search_list: list[int], value: int):
    if not search_list:
        raise ValueError('value not in array')
    min_val = 0 
    max_val = len(search_list) -1 
    if value > search_list[max_val] or value < search_list[min_val]:
            raise ValueError('value not in array')
    while min_val <= max_val:
        middle = (min_val + max_val) // 2
        if search_list[middle] > value: 
            max_val = middle - 1
        elif search_list[middle] < value:
            min_val = middle + 1
        else:
            return middle 
    raise ValueError('value not in array')
# Let min = 0 and max = n-1.
# Compute guess as the average of max and min, rounded down (so that it is an integer).
# If array[guess] equals target, then stop. You found it! Return guess.
# If the guess was too low, that is, array[guess] < target, then set min = guess + 1.
# Otherwise, the guess was too high. Set max = guess - 1.
# Go back to step 2.