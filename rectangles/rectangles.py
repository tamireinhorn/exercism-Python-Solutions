
from collections import namedtuple
import re


def rectangles(strings: list[str]) -> int:
    Edge = namedtuple('Edge', ['row', 'start', 'end'])
    true_counter = 0
    edge_pattern = re.compile("\+-*(?=\+)") # An edge is a + sign, followed by maybe a few -, and then finished by a +.
    all_corners = []
    for index, row in enumerate(strings):
        edges = list(re.finditer(edge_pattern, row))
        row_corners = [Edge(index, i.start(), i.end()) for i in edges]
        if len(edges) > 1:
            long_edge = (Edge(index, edges[0].start(), edges[-1].end()))
            row_corners.append(long_edge)
        all_corners.append(row_corners)
    # Completing rectangles:
    # For every pair of corners of a rectangle, we need to make sure that the lines below it are either + or |.
    # This seems to point to us needing the height as well. List of lists does.
    # transposed = list(map(list, zip(*strings)))
    # for row_index, corner_list in enumerate(all_corners):
    #     for corner in corner_list: # The problem here is the assumption that a single corner will be one rectangle, which with sharing is false.
    #         # I guess a simple solution would be to iterate over all possible '+' edges below it???
    #         start_column = "".join(transposed[corner[0]][row_index + 1 :])
    #         stoppage_start_list = re.finditer("\+", start_column)
    #         end_column = "".join(transposed[corner[1]][row_index + 1 :])
    #         stoppage_end_list = re.finditer("\+", end_column)
    #         for stoppage_start_column, stoppage_end_column in zip(stoppage_start_list, stoppage_end_list):
    #             stoppage_start_column, stoppage_end_column = stoppage_start_column.start(), stoppage_end_column.start() 
    #             start_set = set(start_column[:stoppage_start_column+1])
    #             end_set = set(end_column[:stoppage_end_column+1])
    #             full_set = start_set.union(end_set)
    #             print(2)
    #             if (
    #                 '-' not in full_set
    #                 and ' ' not in full_set
    #                 and stoppage_end_column >= 0
    #                 and stoppage_start_column >= 0
    #                 and stoppage_start_column == stoppage_end_column
    #             ):
    #                 true_counter += 1
    #         # Everything below the edge.
    return true_counter
