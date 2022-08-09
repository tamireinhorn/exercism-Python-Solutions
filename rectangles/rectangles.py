from collections import namedtuple
import re

Edge = namedtuple("Edge", ["row", "start", "end"])
def _edge_ordering(strings: list[str], is_border: bool):
    all_corners = []

    undesired_symbols = [' ']
    if is_border:
        undesired_symbols.append('-')
    for row_index, row in enumerate(strings):
        edges = [i.start() for i in re.finditer('\+', row)]
        for index, edge in enumerate(edges): # Get all '+' signs.
            row_corners = [Edge(row_index, edge, next_edge) for next_edge in edges[index+1:] if not any(symbol in set(row[edge:next_edge]) for symbol in undesired_symbols)] # Get the following + and they are edges.
            # However, we need to verify that from edge to next edge, there are no breaks.
            all_corners += row_corners
    return all_corners


def rectangles(strings: list[str]) -> int:
   
    true_counter = 0
    transposed = ["".join(i) for i in map(list, zip(*strings))]
    # For every pair of corners of a rectangle, we need to make sure that the lines below it are either + or |.
    all_corners = _edge_ordering(strings, False)
    all_borders = _edge_ordering(transposed, True)
   
    for edge in all_corners:
        # Get all candidates to be the closing part of the rectangle:
        lower_edges = filter(
            lambda e: e.row > edge.row and e.start == edge.start and e.end == edge.end,
            all_corners,
        )
        for lower_edge in lower_edges:
            qualifying_borders = list(
                filter(
                    lambda b: ((b.row == edge.start and b.row == lower_edge.start ) or (b.row == edge.end 
                    and b.row == lower_edge.end)) and b.start == edge.row and b.end == lower_edge.row,
                    all_borders,
                
            ))
            if len(qualifying_borders) == 2:
                true_counter += 1
            print(lower_edge)
        print(edge)
    return true_counter


    # The problem right now is with borders that are corners stacked up!
    
