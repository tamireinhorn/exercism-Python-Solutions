class Record:
    def __init__(self, record_id: int, parent_id: int):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id: int):
        self.node_id = node_id
        self.children = []


def createNode(record: Record) -> Node:
    return Node(record.record_id)


def BuildTree(records: list[Record]) -> Node:
    if not records:
        return
    if (
        max(records, key=lambda x: x.record_id).record_id != len(records) - 1
    ):  # We expect that the last item's id is the length of the list.
        raise ValueError("Record id is invalid or out of order.")
    if (
        min(records, key=lambda x: x.record_id).record_id != 0
    ):  # We also expect that there is a 0 record, which will be the root.
        raise ValueError("Record id is invalid or out of order.")
    records.sort(
        key=lambda x: x.record_id
    )  # Sort the list of records (this is still necessary)
    nodes = list(map(createNode, records))
    for index, parent in enumerate(nodes):  # Iterate over all the nodes.
        for record in records:  # Now, iterate over the sorted records.
            if (
                record.record_id < record.parent_id
            ):  # The error message in the exercise is really weird. The record id is ALWAYS larger than parent, except root.
                raise ValueError(
                    "Node record_id should be smaller than it's parent_id."
                )
            if record.record_id == record.parent_id and record.record_id != 0:
                raise ValueError("Only root should have equal record and parent id.")
            if record.parent_id == index:  # If we are on i == j, then:
                parent.children += list(
                    filter(
                        lambda node: node.node_id == record.record_id
                        and node.node_id != 0,
                        nodes,
                    )
                )
    return nodes[0]
