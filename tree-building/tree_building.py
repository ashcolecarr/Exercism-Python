class Record():
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node():
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records):
    if not records:
        return None

    sorted_records = sorted(records, key=lambda x: x.record_id)
    if sorted_records[-1].record_id != len(sorted_records) - 1:
        raise ValueError('Tree must be continuous')
    elif (sorted_records[0].record_id != 0 or
          sorted_records[0].parent_id != 0):
        raise ValueError('Tree must start with record (0, 0)')

    trees = []
    for i in sorted_records:
        if i.record_id < i.parent_id:
            raise ValueError('Parent id must be lower than child id')
        elif i.record_id == i.parent_id and i.record_id != 0:
            raise ValueError('Tree is a cycle')

        node = Node(i.record_id)
        for j in sorted_records[1:]:
            if j.parent_id == node.node_id: # and not \
                    # (j.record_id == 0 and j.parent_id == 0):
                node.children.append(Node(j.record_id))
        #trees.append(Node(i.record_id))
        trees.append(node)

    # parent = {}
    # for i in sorted_records:
    #     for j in trees:
    #         #if i.record_id == j.node_id:
    #         if i.parent_id == j.node_id:
    #             #parent = j
    #             #break
    #             j.children.append(i)

    #     # for j in sorted_records:
    #     #     if j.parent_id == i.record_id:
    #     #         for k in trees[1:]:
    #     #             if j.record_id == k.node_id:
    #     #                 parent.children.append(k)

    return trees[0]
