from copy import copy

def saddle_points(matrix):
    if not matrix:
        return []
    if len(set(map(len, matrix))) != 1:
        raise ValueError('irregular matrix')
    # Saddle point is a point where the element is the biggest in its row but the smallest in its column. 
    # First off, I guess I'd create columns:
    # We revert the matrix 
    copy_matrix = [copy(row) for row in matrix[::-1]]
    columns = [[] for i in range(len(copy_matrix[0]))]
    while copy_matrix:
        current = copy_matrix.pop()
        for column in columns:
            column.append(current.pop())
    saddles = []
    # Iterate over columns 
    for column_index, column in enumerate(columns[::-1]):
        column_min = min(column) # The minimal is our candidate for saddle
        row_indices = (index for index, value in enumerate(column) if value == column_min) # Get every time the minimal is in that column
        for row_index in row_indices:
            if max(matrix[row_index]) == column_min: # We get the row and see if its max is that min, if so, it's a saddle.
                point = {"row": row_index + 1, "column": column_index + 1}
                saddles.append(point)
    return saddles
