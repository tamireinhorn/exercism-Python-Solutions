def square_of_sum(number):
   return (0.5 * number * (number+1)) ** 2


def sum_of_squares(number):
    return (1/6) * (number * (number+1) * (2 * number + 1))
  


def difference_of_squares(number): 
    return square_of_sum(number) - sum_of_squares(number)
