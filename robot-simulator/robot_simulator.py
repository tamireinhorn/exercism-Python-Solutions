# Globals for the directions
# Change the values as you see fit
EAST = 'E'
NORTH = 'N'
WEST = 'W'
SOUTH = 'S'

class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.coordinates = (x_pos, y_pos)

    def move(self, movement_string):
        dir = self.direction
        x, y = self.coordinates
        for movement in movement_string:
            if movement == "R":
                if dir == NORTH:
                    dir = EAST
                elif dir == EAST:
                    dir = SOUTH
                elif dir == WEST:
                    dir = NORTH
                else:
                    dir = WEST
            elif movement == "L":
                if dir == NORTH:
                    dir = WEST
                elif dir == EAST:
                    dir = NORTH
                elif dir == WEST:
                    dir = SOUTH
                else:
                    dir = EAST
            if movement == "A":
                if dir == NORTH:
                    y += 1
                elif dir == EAST:
                    x += 1
                elif dir == SOUTH:
                    y -= 1
                else:
                    x -= 1
        self.direction = dir
        self.coordinates = x, y 