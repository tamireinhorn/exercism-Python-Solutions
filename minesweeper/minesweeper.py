def nearby_cells(number_of_rows, number_of_columns, index: tuple):
    """"
    Receives the size of the diagram and an index and returns the cells that are close to it.
    
    """
    row_index = index[0]
    column_index = index[1]
    is_upper_vertical_edge = row_index == 0
    is_lower_vertical_edge = row_index == number_of_rows - 1
    is_left_horizontal_edge = column_index == 0
    is_right_horizontal_edge = column_index == number_of_columns -1
    below =  [(row_index+1, column_index)]
    above =  [(row_index-1, column_index)]
    right =  [(row_index, column_index + 1)]
    left =   [(row_index, column_index -1)]
    above_left = [(row_index-1, column_index-1)]
    above_right =  [(row_index-1, column_index+1)]
    below_left =  [(row_index+1, column_index-1)]
    below_right =  [(row_index+1, column_index+1)]
    if number_of_rows == 1:
        if is_left_horizontal_edge:
            answer = right
        elif is_right_horizontal_edge:
            answer = left
        else:
            answer = left + right
    elif number_of_columns == 1:
        if is_upper_vertical_edge:
            answer = below
        elif is_lower_vertical_edge:
            answer = above
        else:
            answer = above + below
    else:
        if is_upper_vertical_edge and is_left_horizontal_edge:
            answer = below + right + below_right
        elif is_upper_vertical_edge and is_right_horizontal_edge:
            answer = below + left + below_left
        elif is_lower_vertical_edge and is_left_horizontal_edge:
            answer = above + right + above_right
        elif is_lower_vertical_edge and is_right_horizontal_edge:
            answer = above + left + above_left
        elif is_upper_vertical_edge:
            answer = below + right + below_right + left + below_left
        elif is_lower_vertical_edge:
            answer = above + right + left + above_left + above_right
        elif is_left_horizontal_edge:
            answer = above + below + right + above_right + below_right
        elif is_right_horizontal_edge:
            answer = above + below + left + above_left + below_left
        else:
            answer = above + above_right + above_left + below_left + below_right + below + left + right
    return answer


def annotate(minefield):
    if not minefield or len(minefield[0]) == 0:
        return minefield
    number_of_rows = len(minefield)
    number_of_columns = len(minefield[0])
    if len(set(list(map(len, minefield)))) > 1:
        raise ValueError("The board is invalid with current input.")
    annotation = [ [ 0 for i in range(number_of_columns) ] for i in range(number_of_rows) ]
    for row_number, row in enumerate(minefield):
        for column_number, element in enumerate(row):
            if element == '*': # Is mine.
                annotation[row_number][column_number] = '*'
                #Now we add +1 to the corresponding guys, given by the function
                next_squares = nearby_cells(number_of_rows, number_of_columns, (row_number, column_number))
                for squares in next_squares:
                    row_index = squares[0]
                    column_index = squares[1]
                    if minefield[row_index][column_index] != '*':
                        annotation[row_index][column_index] += 1
            elif element != ' ':
                raise ValueError("The board is invalid with current input.")
    for row_number, row in enumerate(annotation):
        annotation[row_number] = ''.join(list(map(str, row))).replace('0', ' ')
    return annotation


