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

    def from_pov(self, from_node):
        if self.label == from_node:
            return self # Base case needs nothing more
        path = self.path_from_self(from_node)
        if not path: # If the path is empty, there is no possible path to it and thus no reorientation.
            raise ValueError('Tree could not be reoriented')
        # The base case requires us to iterate on two connected nodes at a time:
        for first_node, second_node in zip(path[0:], path[1:]):
            # The first node is now the children of the second, so:
            first_node.children.remove(second_node) # The first node loses the second as child
            second_node.children.append(first_node) # Now the second node is the father of the second.
        return path[-1] # The last node in path is the from node where the new root is.


    def path_to(self, from_node, to_node):
        # Reorient tree:
        new_tree = self.from_pov(from_node)
        path = new_tree.path_from_self(to_node)
        if path:
            return [node.label for node in path]
        else:
            raise ValueError('No path found')

    def path_from_self(self, to_node: str) -> list['Tree']:
        """Builds a path from the root node to a specific node.

        Args:
            to_node (str): Node where we want to get to.

        Returns:
            _type_: _description_
        """
        if self.label == to_node: # Base case for recursion, we spit out the actual tree itself because we're there.
            return [self]
        for child in self.children:
            temp = child.path_from_self(to_node) # Apply the same method again, recursively
            if temp:
                return [self] + temp
        return [] # Empty otherwise.