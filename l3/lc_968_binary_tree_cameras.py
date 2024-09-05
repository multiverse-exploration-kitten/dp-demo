# Definition for a binary tree node.
import sys
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        result = self.dfs(root)
        return min(result[1:])

    def dfs(self, node):
        if not node:
            return 0, 0, sys.maxsize

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        dp0 = left[1] + right[1]
        dp1 = min(left[2] + min(right[1:]), right[2] + min(left[1:]))
        dp2 = 1 + min(left) + min(right)

        return dp0, dp1, dp2
