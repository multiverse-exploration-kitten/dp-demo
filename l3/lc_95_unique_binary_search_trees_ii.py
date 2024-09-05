# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []

        dp = self.initialize_dp(n)

        for number_of_nodes in range(2, n + 1):
            self.fill_dp(dp, n, number_of_nodes)

        return dp[1][n]

    def initialize_dp(self, n: int) -> List[List[List[Optional[TreeNode]]]]:
        """Initialize the dp table."""
        dp = [[[] for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i][i] = [TreeNode(i)]
        return dp

    def fill_dp(
        self, dp: List[List[List[Optional[TreeNode]]]], n: int, number_of_nodes: int
    ) -> None:
        """Fill the dp table for all ranges of number_of_nodes."""
        for start in range(1, n - number_of_nodes + 2):
            end = start + number_of_nodes - 1
            self.fill_range(dp, start, end)

    def fill_range(
        self, dp: List[List[List[Optional[TreeNode]]]], start: int, end: int
    ) -> None:
        """Fill the dp table for the specific range from start to end."""
        for root_val in range(start, end + 1):
            left_subtrees = dp[start][root_val - 1] if root_val != start else [None]
            right_subtrees = dp[root_val + 1][end] if root_val != end else [None]

            self.add_trees(dp, start, end, root_val, left_subtrees, right_subtrees)

    def add_trees(
        self,
        dp: List[List[List[Optional[TreeNode]]]],
        start: int,
        end: int,
        root_val: int,
        left_subtrees: List[Optional[TreeNode]],
        right_subtrees: List[Optional[TreeNode]],
    ) -> None:
        """Add the trees for each combination of left and right subtrees."""
        for left in left_subtrees:
            for right in right_subtrees:
                root = TreeNode(root_val, left, right)
                dp[start][end].append(root)
