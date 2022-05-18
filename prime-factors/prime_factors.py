def factors(value):
    factor_list = []
    current_value = value
    current_factor = 2
    while current_value > 1:
        quotient, rest = divmod(current_value, current_factor)
        if rest == 0:
            factor_list.append(current_factor)
            current_value = quotient
        else:
            current_factor += 1
    return factor_list
 