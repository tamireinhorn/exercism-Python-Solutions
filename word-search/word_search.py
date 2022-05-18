import re
from collections import defaultdict


def is_positive(x):
    if x > 0:
        return 1
    else:
        return 0 


def rows_columns(word, input, is_row):
    reversed_word = word[::-1]
    for index, row in enumerate(input):
        match = re.search(word, row)
        reverse_match = re.search(reversed_word, row)
        if match:
            a = Point(index, match.start())
            b = Point(index, match.end()-1)
            if is_row:
                a, b = a.reverse(), b.reverse()
            return a,b
        elif reverse_match:
            a = Point(index, reverse_match.start())
            b = Point(index, reverse_match.end()-1)
            if is_row:
                a, b = a.reverse(), b.reverse()
            return b, a


def diagonal_search(word, input, bottom_left, rows):
    reversed_word = word[::-1]
    for key, diagonal in input.items():
        match = re.search(word, diagonal)
        reverse_match = re.search(reversed_word, diagonal)
        f = is_positive(key)
        g = is_not_positive(f)
        if match:
            a = Point(-(key * g) + match.start(),(key * f)  + match.start())
            b = Point(-(key * g) + match.end() -1,(key * f) +  match.end() - 1)
            if bottom_left:
                a = Point(rows - 1 - (key * g) - match.start(), (key * f) + match.start())
                b = Point(rows -1 - (key * g) - (match.end() -1), (key * f) + match.end() -1)
            return a, b
        if reverse_match:
            a = Point(-(key * g) + reverse_match.start(), (key * f ) + reverse_match.start())
            b = Point(-(key * g) + reverse_match.end()-1, ( key * f ) + reverse_match.end() - 1)
            if bottom_left:
                a = Point(rows - 1 + (key * g) - reverse_match.start(), (key * f ) + reverse_match.start())
                b = Point(rows - 1 + (key * g) - (reverse_match.end() -1), (key * f) + reverse_match.end() - 1)
            return b, a


def create_diagonals(puzzle):
    rows = len(puzzle)
    matrix =[list(row) for row in puzzle]
    diagonal1 = defaultdict(list) # For the top right to bottom left
    diagonal2 = defaultdict(list) # For the top left to bottom right
    for i in range(rows):
        for j in range(rows):
            diagonal1[i-j].append(matrix[i][j])
            diagonal2[i+j].append(matrix[i][j])
    diagonal1 = {item[0]: ''.join(item[1]) for item in diagonal1.items()}
    #These diagonals follow this pattern:
    #If it's 0, it starts at (0,0), adding (1, 1)
    # If it's positive, let i be the index of the diagonal.
    # Since the POSITIVE diagonals are the ones UNDER the main one, they start at (0, i)
    # They grow adding (1,1)
    # The negative ones are ABOVE the main one, and start at (-i, 0).
    # All you do is get its beggining and add (i,i) * match.start()
    # The end position is its and add (i,i) * match.end() - 1
    diagonal2 = {item[0] - (rows -1) : ''.join(item[1]) for item in diagonal2.items()}
    # These diagonals always add (-1, 1).
    # As before, 0 is the main one, now starting at (n-1, 0)
    # Positive ones are under the main one, starting at (n-1, i)
    # Negative ones are above the main one, starting at (n-1 +i, 0)
    return diagonal1, diagonal2
is_not_positive = lambda x: 1 - x


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def reverse(self):
        return Point(self.y, self.x)

class WordSearch:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.rows = len(puzzle)
        self.columns = len(puzzle[0])


    def search(self, word):
        rows = self.rows
        puzzle = self.puzzle
        answer = rows_columns(word, puzzle, 1) #Row search
        if answer:
            return answer
        columns = [''.join([puzzle[row][column] for row in range(rows)]) for column in range(self.columns)]
        answer = rows_columns(word, columns, 0) #Column search
        if answer:
            return answer
        diagonal1, diagonal2 = create_diagonals(puzzle)
        answer = diagonal_search(word, diagonal1, 0, rows)
        if answer:
            return answer
        answer = diagonal_search(word, diagonal2, 1, rows)
        if answer:
            return answer