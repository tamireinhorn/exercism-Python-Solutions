def leap_year(year):
    is_divisible_4 = year % 4 == 0
    is_divisible_100 = year % 100 == 0
    is_divisible_400 = year % 400 == 0
    if is_divisible_4:
        if is_divisible_100:
            if is_divisible_400:
                return True
            else:
                return False
        return True
    else:
        return False
