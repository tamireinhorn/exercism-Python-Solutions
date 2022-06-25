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
        if self.label == from_node:
            return self
        # For a simple one, you have parent -> [x, sibling]. So you run down a queue with BFS until you find the node
        queue = [self]
        stack = [self]
        while queue:
            first_of_the_line = queue[0]
            queue += first_of_the_line.children
            stack += first_of_the_line.children
            if first_of_the_line.label == from_node:
                break
            queue = queue[1:]
        # Once the node is found, you get it's parent, which should be the first guy in the stack?
        papa = stack[0]
        papa.children = list(filter(lambda node: node.label != from_node, papa.children))
        new_tree = Tree(from_node, children= papa)
        return new_tree

    def path_to(self, from_node, to_node):
        pass
