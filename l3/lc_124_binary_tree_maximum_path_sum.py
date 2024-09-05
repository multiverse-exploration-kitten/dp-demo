# Definition for a binary tree node.
import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = -sys.maxsize
        self.dfs(root)

        return self.ans

    def dfs(self, root):
        if root is None:
            return 0

        left_max = max(self.dfs(root.left), 0)
        right_max = max(self.dfs(root.right), 0)
        curr_node_sum = root.val + left_max + right_max
        self.ans = max(self.ans, curr_node_sum)

        return root.val + max(left_max, right_max)
