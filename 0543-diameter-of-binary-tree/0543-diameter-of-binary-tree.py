from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def height(node: Optional[TreeNode]) -> int:
            nonlocal max_diameter
            if not node:
                return -1  # Edge count convention: empty subtree has height -1

            left_h = height(node.left)
            right_h = height(node.right)

            # Longest path with `node` as the highest point (turning point)
            current_diameter = (left_h + 1) + (right_h + 1)
            if current_diameter > max_diameter:
                max_diameter = current_diameter

            return 1 + max(left_h, right_h)

        height(root)
        return max_diameter