from collections import namedtuple
import re

Edge = namedtuple("Edge", ["row", "start", "end"])
def _edge_ordering(strings: list[str]):
    all_corners = []
    for row_index, row in enumerate(strings):
        edges = [i.start() for i in re.finditer('\+', row)]
        for index, edge in enumerate(edges):
            row_corners = [Edge(row_index, edge, next_edge) for next_edge in edges[index+1:]]
            all_corners += row_corners
    return all_corners


def rectangles(strings: list[str]) -> int:
   
    true_counter = 0
    border_pattern = re.compile(
        "\+\|*(?=\+)"
    )  # A border is a + sign, followed by maybe a few -, and then finished by a +.
    transposed = ["".join(i) for i in map(list, zip(*strings))]
    # For every pair of corners of a rectangle, we need to make sure that the lines below it are either + or |.
    all_corners = _edge_ordering(strings)
    all_borders = _edge_ordering(transposed)
   
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
    
