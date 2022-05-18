import re


TREE_BASICS = "\(.*\)"
NODE = ";"

class SgfTree:
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for key, value in self.properties.items():
            if key not in other.properties:
                return False
            if other.properties[key] != value:
                return False
        for key in other.properties.keys():
            if key not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for child, other_child in zip(self.children, other.children):
            if child != other_child:
                return False
        return True

    def __ne__(self, other):
        return not self == other


def node_process(node):
    node = re.sub('\t', ' ', node) # Tabs become space.
    value_string = r'\[\w+]|\[.*\w+.*\]|\[.*\w+\]\[\w+.*\]' # A value is always one of these:
    # It has [string] but there could be 'messy' things before or after it.
    # I've yet to make '.*' also accept that nothing before it works, so you have to prevent all 4 possibilities.
    property_value = re.findall(f'[A-Za-z]+(?:{value_string})+', node, flags= re.DOTALL) # A property is in the format 'string[string]', basically.
    if node and not re.search(value_string, node, flags = re.DOTALL): # If there's something in the node BUT no delimiter
        raise ValueError("properties without delimiter")
    properties_dict = {} # Create an empty dict to be filled. 
    for p in property_value: # Iterate over the property-value pairs found. Properties can have multiple values, like A[B][C]
        split_property = re.split(f'({value_string})',p, flags = re.DOTALL) # Split by the values.
        property = split_property[0] # The first guy is always the property itself.
        if not str.isupper(property): # If the property itself is not uppercase
            raise ValueError("property must be in uppercase")
        values = [re.sub(r"(?<!\\)\[|(?<!\\)\]|\\", "", element) for element in split_property[1:] if element] # The non-empty rest of the list is values and we just clean them.
        # This sub is complex, if we have "\" (which is written as \\ due to escaping) before '\[' or '\]'
        # we don't WANT to remove them, because the \ before SIGNALS to keep the character.
        # So we just remove '\\' because we don't need the signaling no more. 
        properties_dict.update({property: values}) # Then we add the property and its values to the dict.

    return properties_dict # Done, the node is returned as a dictionary.


def tree_process(tree):
    clean_tree = re.sub("\(|\)", "", tree) # Remove the parenthesis to clean the tree string.
    node_split = re.split(NODE, clean_tree)[1:] # Split by the node delimiter to get the nodes.
    properties = node_process(node_split[0]) # The first part of the node is the property.
    if len(node_split) == 1:
        children = {} # If there's just a single node in the tree, children is empty.
    else:
        children = list(map(node_process, node_split[1:])) # If there's more than 1 node, we process them all as children.
    return properties, children


def parse(input_string):
    # A tree starts with ( and ends with ).
    # A node is given by ";". 
    tree_search = re.search(TREE_BASICS, input_string, flags = re.DOTALL)
    node_search = re.search(NODE, input_string)
    tree_split = re.split("(?=\()", input_string)[1:]
    if not tree_search:
        raise ValueError("tree missing")
    if not node_search:
        raise ValueError("tree with no nodes")
    if len(tree_split) == 1: # If it's just a single, simple tree:
        properties, children = tree_process(tree_split[0]) # We get the dictionaries.
        children = [SgfTree(child) for child in children] # The children need to be trees, we take that.
        answer = SgfTree(properties=properties, children=children)
    else:
        properties, _  = tree_process(tree_split[0]) # If it's more than a tree, only the properties will be here.
        children = [SgfTree(prop, child) for prop, child in (map(tree_process, tree_split[1:]))] # The remaining trees will be processed as trees and made children.
        answer = SgfTree(properties= properties, children= children)
    return answer
