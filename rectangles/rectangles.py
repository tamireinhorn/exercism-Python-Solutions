from copy import copy
import re

# |\
def rectangles(strings: list[str]) -> int:
    true_counter = 0
    edge_pattern = re.compile("\+-*(?=\+)")
    all_corners = []
    for row in strings:
        edges = list(re.finditer(edge_pattern, row))
        row_corners = [(i.start(), i.end()) for i in edges]
        if len(edges) > 1:
            long_edge = (edges[0].start(), edges[-1].end())
            row_corners.append(long_edge)
        all_corners.append(row_corners)
    # Completing rectangles:
    # For every pair of corners of a rectangle, we need to make sure that the lines below it are either + or |.
    # This seems to point to us needing the height as well. List of lists does.
    transposed = list(map(list, zip(*strings)))
    for row_index, corner_list in enumerate(all_corners):
        for corner in corner_list: # The problem here is the assumption that a single corner will be one rectangle, which with sharing is false.
            # I guess a simple solution would be to iterate over all possible '+' edges below it???
            start_column = "".join(transposed[corner[0]][row_index + 1 :])
            stoppage_start_column = start_column.find("+")
            end_column = "".join(transposed[corner[1]][row_index + 1 :])
            stoppage_end_column = end_column.find("+")
            master_set = set(["|", "+"])
            start_set = set(start_column[:stoppage_start_column+1])
            end_set = set(end_column[:stoppage_end_column+1])
            full_set = start_set.union(end_set)
            if (
                '-' not in full_set
                and ' ' not in full_set
                and stoppage_end_column >= 0
                and stoppage_start_column >= 0
            ):
                true_counter += 1
            # Everything below the edge.
    return true_counter
