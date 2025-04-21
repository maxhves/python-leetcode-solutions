"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.
"""
from typing import Optional, List

from common.tree_node import TreeNode, build_tree


# region Solution

def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    nodes = []

    def inorder_traverse(node: Optional[TreeNode]):
        if not node:
            return

        inorder_traverse(node.left)
        nodes.append(node.val)
        inorder_traverse(node.right)

    inorder_traverse(root)
    return nodes


# endregion

# region Tests

# [1, 3, 2]
print(inorder_traversal(build_tree([1, None, 2, 3])))

# [4, 2, 6, 5, 7, 1, 3, 9, 8]
print(inorder_traversal(build_tree([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9])))

# []
print(inorder_traversal(build_tree([])))

# [1]
print(inorder_traversal(build_tree([1])))

# endregion
