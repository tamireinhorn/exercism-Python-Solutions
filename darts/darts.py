OUTER_RADIUS = 10
MIDDLE_RADIUS = 5
INNER_RADIUS = 1
def inside_circle(x, y, r):
    return x**2 + y**2 <= r**2
def score(x, y):
    if inside_circle(x,y,INNER_RADIUS):
        return 10
    elif inside_circle(x,y,MIDDLE_RADIUS):
        return 5
    elif inside_circle(x,y,OUTER_RADIUS):
        return 1
    else:
        return 0 
