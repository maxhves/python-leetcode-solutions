"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
"""
from typing import Optional

from common.node import Node, build_graph_from_list


# region Solution

def clone_graph(node: Optional[Node]) -> Optional[Node]:
    cloned_nodes = {}

    def dfs(node: Node) -> Optional[Node]:
        if node in cloned_nodes:
            return cloned_nodes[node]

        clone = Node(node.val)
        cloned_nodes[node] = clone
        for neighbor in node.neighbors:
            clone.neighbors.append(dfs(neighbor))

        return clone

    return dfs(node) if node else None


# endregion

# region Tests

print(clone_graph(build_graph_from_list([[2, 4], [1, 3], [2, 4], [1, 3]])))

# endregion
