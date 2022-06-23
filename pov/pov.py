from json import dumps


class Tree:
    def __init__(self, label, children=None):
        self.label = label
        self.children = children if children is not None else []

    def __dict__(self):
        return {self.label: [c.__dict__() for c in sorted(self.children)]}

    def __str__(self, indent=None):
        return dumps(self.__dict__(), indent=indent)

    def __lt__(self, other):
        return self.label < other.label

    def __eq__(self, other):
        return self.__dict__() == other.__dict__()

    def find_node(self, node):
        # We can only reroot a tree once we find the desired node.
        if self.label == node:
            return True
        queue = [self]
        while queue:
            first_of_the_line = queue[0]
            queue += first_of_the_line.children
            queue = queue[1:]

    def from_pov(self, from_node):
        self.find_node(from_node)

    def path_to(self, from_node, to_node):
        pass
