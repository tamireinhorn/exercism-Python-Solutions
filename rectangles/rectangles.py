from collections import namedtuple
import re


def rectangles(strings: list[str]) -> int:
    Edge = namedtuple("Edge", ["row", "start", "end"])
    true_counter = 0
    edge_pattern = re.compile(
        "\+-*(?=\+)"
    )  # An edge is a + sign, followed by maybe a few -, and then finished by a +.
    border_pattern = re.compile(
        "\+\|*(?=\+)"
    )  # A border is a + sign, followed by maybe a few -, and then finished by a +.
    transposed = ["".join(i) for i in map(list, zip(*strings))]
    # For every pair of corners of a rectangle, we need to make sure that the lines below it are either + or |.
    all_corners = []
    all_borders = []
    for index, row in enumerate(strings):
        edges = list(re.finditer(edge_pattern, row))
        row_corners = [Edge(index, i.start(), i.end()) for i in edges]
        if len(edges) > 1:
            long_edge = Edge(index, edges[0].start(), edges[-1].end())
            row_corners.append(long_edge)
        all_corners += row_corners
    for index, row in enumerate(transposed):
        borders = list(re.finditer(border_pattern, row))
        column_corners = [Edge(index, i.start(), i.end()) for i in borders]
        if len(borders) > 1:
            long_border = Edge(index, borders[0].start(), borders[-1].end())
            column_corners.append(long_border)
        all_borders += column_corners
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
