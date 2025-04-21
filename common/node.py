class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def build_graph_from_list(adj_list):
    if not adj_list:
        return {}

    nodes = {}

    for i in range(len(adj_list)):
        node_val = i + 1
        nodes[node_val] = Node(node_val)

    for i in range(len(adj_list)):
        current_node_val = i + 1
        current_node = nodes[current_node_val]

        for neighbor_val in adj_list[i]:
            if neighbor_val in nodes:
                current_node.neighbors.append(nodes[neighbor_val])

    return nodes
