import re
#|\
def rectangles(strings: list[str]) -> int:
    counter = 0
    edge_pattern = re.compile('\+-*(?=\+)')
    corners = []
    for row in strings:
        edges = list(re.finditer(edge_pattern, row))
        if len(edges) > 1:
            long_edge = (edges[0].start(), edges[-1].end())
            if long_edge in corners:
                counter += 1
            corners.append(long_edge)
        for match in edges:
            counter += len(list(i for i in corners if i == match.span()))
            corners.append(match.span())
        print(2)

    return counter
