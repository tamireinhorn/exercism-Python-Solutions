import re

#|
def rectangles(strings: list[str]) -> int:
    edge_list = []
    line_list = []
    for string in strings:
        edge_match = re.finditer('\+', string)
        # You start with edges, and you expect to see a line from them until a next set of equal edges.
        if edge_match:
            edge_list.append([match.start() for match in edge_match])
        line_match = re.finditer('\|', string)
        if line_match:
            line_list.append([match.start() for match in line_match])
        pass
    pass


# I think a stack like the one for the bracket balancing makes a lot of sense
