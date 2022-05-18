from collections import Counter
def is_valid_triangle(sides):
    valid_sides = all(side > 0 for side in sides)

    full_inequality = max(sides) <= sum(sides) - max(sides)
    #You don't need to check all sides of the triangle.
    #Rather, you can verify that the BIGGEST side still obeys the inequality.
    #It can be shown mathematically that if x1 > x2 > x3 and we guarantee that the inequality holds for x1,
    #it holds for all other sides, IF they are positive, which is already verified.
    return valid_sides and full_inequality
def equilateral(sides):
    return len(Counter(sides)) == 1 and is_valid_triangle(sides)


def isosceles(sides):
     return len(Counter(sides)) <= 2 and is_valid_triangle(sides)

def scalene(sides):
    return len(Counter(sides)) > 2 and is_valid_triangle(sides)
