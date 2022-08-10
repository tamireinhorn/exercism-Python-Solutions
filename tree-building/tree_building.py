class Record:
    def __init__(self, record_id: int, parent_id: int):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id: int):
        self.node_id = node_id
        self.children = []


def BuildTree(records: list[Record]):
    if not records:
        return
    records.sort(key=lambda x: x.record_id) # Sort the list of records
    ordered_id = [i.record_id for i in records] # Then get their id, in order.
    if ordered_id[-1] != len(ordered_id) - 1: # We expect that the last item's id is the length of the list.
        raise ValueError("Record id is invalid or out of order.")
    if ordered_id[0] != 0: # We also expect that there is a 0 record, which will be the root.
        raise ValueError("Record id is invalid or out of order.")
    trees = []
    parent = {}
    for i, j in zip(range(len(ordered_id)), records): # Updated this to a zip. This ONLY serves for errors, and then creating the list of Nodes of ordered ids.
            if j.record_id < j.parent_id: # The error message in the exercise is really weird. The record id is ALWAYS larger than parent, except root.
                raise ValueError("Node record_id should be smaller than it's parent_id.")
            if j.record_id == j.parent_id and j.record_id != 0:
                raise ValueError("Only root should have equal record and parent id.")
            trees.append(Node(ordered_id[i]))
    for i in range(len(ordered_id)): # Iterate over the range of ids.
        for j in trees: # Then, iterate over the list of nodes.
            if i == j.node_id: # If they are the same, the parent variable is the j-th Node.
                parent = j
        for j in records: # Now, iterate over the sorted records.
            if j.parent_id == i: # If we are on i == j, then:
                for k in trees: # Iterate over fucking trees again
                    if j.record_id == k.node_id and k.node_id != 0: # If it's not the root and the current ordered record's id is the same as the Node, then that's the child.
                        child = k
                        parent.children.append(child) # You get that node, get the list of it's children then add the k-th Node to it. 
    return trees[0]

# I might not need a binary tree algorithm after all.
# I literally already have the tree's mapping INSIDE of the records. 
# All I need is to start assembling it.