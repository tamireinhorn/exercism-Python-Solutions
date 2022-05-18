def spiral_matrix(size):
    max_element = size * size
    current_element = 1
    left_pointer, left_size = 0, size
    right_pointer, right_size = 0, size
    up_pointer, up_size = 0, size - 1
    down_pointer, down_size = 0, size 
    # Initialize a n x n matrix of None. 
    full_matrix = [[None for i in range(size)] for i in range(size)]
    while max_element:
        print('Check full matrix')
        #On a spiral matrix, the left to right movement will start from the current element of the spiral OR the first None, whichever comes first:
        none_index = full_matrix[left_pointer].index(None)
        if current_element in full_matrix[left_pointer]:
            none_index = min(none_index, full_matrix[left_pointer].index(current_element))
        # We want to replace that specific row of the matrix, given by left pointer
        # However, we do not want to replace ALL of it. We want to go from the desired index to the size of that movement, which starts at n and decreases by 1.
        # We replace it by the range of current element all the way to current element + size of the arrow... OR the max element, whichever is smaller.
        # This is just to prevent the final arrow of being too long.
        full_matrix[left_pointer][none_index:left_size] = list(range(current_element,min(current_element + left_size, max_element+1)))
        # Update current element and left movement pointers.
        current_element = full_matrix[left_pointer][-1 -left_pointer]
        left_pointer += 1
        left_size -= 1
        # If it's done, it's done.
        if current_element == max_element:
            break
        #Then we do from up to down:
        # So we just use the pointers to get the rows we need to change and change the same position in all, simulating a column being filled
        for row in full_matrix[down_pointer:][:down_size]:
            row[-1 - down_pointer]  = current_element
            current_element += 1
        # Given the for loop, it will add 1 to current element before ending, so we just correct for that.
        current_element -= 1
        down_size -= 2
        down_pointer += 1
        if current_element == max_element:
            break
        #Now from right to left:
        # We want to fill it starting from the first None. 
        none_index = full_matrix[-1 - right_pointer].index(None)
        # Since it's from right to left, we fill it with the desired range and the elements that were already there!
        full_matrix[-1 - right_pointer][none_index:] = list(range(current_element + right_size -1, current_element -1, -1)) + full_matrix[-1 - right_pointer][-1::][:right_pointer]
        current_element = full_matrix[-1 - right_pointer][none_index]
        if current_element == max_element:
            break
        right_size -= 2
        right_pointer += 1
        #Now from down to up, we start at the bottom of the matrix and use the pointers to see which rows will be affected, and where.
        for row in full_matrix[::-1][up_pointer:up_size]:
            row[up_pointer] = current_element
            current_element += 1
        # As with the previous column loop, we need to take the extra +1 the for loop gives us. 
        current_element -= 1
        up_size -= 1
        up_pointer += 1
        if current_element == max_element:
            break
    return full_matrix
