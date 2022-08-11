class Record:
    def __init__(self, record_id: int, parent_id: int):
        self.record_id = record_id
        self.parent_id = parent_id

class Node:
    def __init__(self, node_id: int):
        self.node_id = node_id
        self.children = []

def createNode(record: Record):
    return Node(record.record_id)

def BuildTree(records: list[Record]):
    if not records:
        return
    records.sort(key=lambda x: x.record_id) # Sort the list of records
    # Neither of the checks below require ordering, just some clever min and max.
    if max(records, key=lambda x: x.record_id).record_id != len(records) - 1: # We expect that the last item's id is the length of the list.
        raise ValueError("Record id is invalid or out of order.")
    if min(records, key=lambda x: x.record_id).record_id != 0: # We also expect that there is a 0 record, which will be the root.
        raise ValueError("Record id is invalid or out of order.")
    trees = list(map(createNode, records))
    parent = {}
    for index, parent in enumerate(trees): # Iterate over the range of ids.
        for record in records: # Now, iterate over the sorted records.
            if record.record_id < record.parent_id: # The error message in the exercise is really weird. The record id is ALWAYS larger than parent, except root.
                raise ValueError("Node record_id should be smaller than it's parent_id.")
            if record.record_id == record.parent_id and record.record_id != 0:
                raise ValueError("Only root should have equal record and parent id.")
            if record.parent_id == index: # If we are on i == j, then:
                for tree in trees: # Iterate over fucking trees again
                    if record.record_id == tree.node_id and tree.node_id != 0: # If it's not the root and the current ordered record's id is the same as the Node, then that's the child.
                        child = tree
                        parent.children.append(child) # You get that node, get the list of it's children then add the k-th Node to it. 
    return trees[0]

# I might not need a binary tree algorithm after all.
# I literally already have the tree's mapping INSIDE of the records. 
# All I need is to start assembling it.