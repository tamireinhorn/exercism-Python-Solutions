class Record:
    def __init__(self, record_id: int, parent_id: int):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id: int):
        self.node_id = node_id
        self.children = []


def BuildTree(records: list[Record]):
    root = None
    records.sort(key=lambda x: x.record_id) # Sort the list of records
    ordered_id = [i.record_id for i in records] # Then get their id, in order.
    if records: # If the list is not empty
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
    for i in range(len(ordered_id)):
        for j in trees:
            if i == j.node_id:
                parent = j
        for j in records:
            if j.parent_id == i:
                for k in trees:
                    if k.node_id == 0:
                        continue
                    if j.record_id == k.node_id:
                        child = k
                        parent.children.append(child)
    if len(trees) > 0:
        root = trees[0]
    return root
