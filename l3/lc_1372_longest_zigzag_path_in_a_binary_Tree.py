from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        max_length = [0]
        self.dfs(root, False, 0, max_length)
        self.dfs(root, True, 0, max_length)
        return max_length[0]

    def dfs(self, node, go_left, steps, max_length):
        if node:
            max_length[0] = max(max_length[0], steps)
            if go_left:
                self.dfs(node.left, False, steps + 1, max_length)
                self.dfs(node.right, True, 1, max_length)
            else:
                self.dfs(node.left, False, 1, max_length)
                self.dfs(node.right, True, steps + 1, max_length)
