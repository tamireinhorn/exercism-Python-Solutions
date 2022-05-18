from collections import Counter


BOOK_PRICE = 8

def price_discount(discount):
    return (1 - discount) * BOOK_PRICE


def applied_discount(number_of_books):
    if number_of_books == 2:
        discount = 0.05
    elif number_of_books == 3:
        discount = 0.1
    elif number_of_books == 4:
        discount = 0.2
    elif number_of_books == 5:
        discount = 0.25 
    else:
        discount = 0
    return number_of_books * price_discount(discount)


def format_result(number):
    return round(number * 100)

def _recursive_basket(grouped_basket, current_price):
    if len(grouped_basket) == 0:
        return current_price
    maximum_bundle = len(grouped_basket)
    min_eval = sum(grouped_basket) * 1000 * BOOK_PRICE
    for bundle in range(1, maximum_bundle+1):
        rest = grouped_basket[bundle:]
        modified = [i -1 for i in grouped_basket[:bundle] if i -1 != 0]
        new_cart = modified + rest
        eval = _recursive_basket(new_cart, current_price + applied_discount(bundle))
        min_eval = min(min_eval, eval)
    return min_eval


def total(basket):
    grouped_basket = [i for i in Counter(basket).values()]
    grouped_basket.sort(reverse= True)
    return format_result(_recursive_basket(grouped_basket, 0))
