# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        # If n is even, no full binary trees can be formed
        if n % 2 == 0:
            return []

        # Initialize a list to store the trees for each odd count of nodes
        dp = [[] for _ in range(n + 1)]
        # A full binary tree with one node is just the root
        dp[1].append(TreeNode(0))

        # Iterate through all odd numbers from 3 to n (since only odd counts can form full binary trees)
        for count in range(3, n + 1, 2):
            for i in range(1, count - 1, 2):
                j = count - 1 - i
                # For each combination of left and right subtree counts, create new trees
                self._combine_subtrees(dp, count, i, j)

        return dp[n]

    def _combine_subtrees(
        self, dp: List[List[TreeNode]], count: int, left_count: int, right_count: int
    ) -> None:
        for left in dp[left_count]:
            for right in dp[right_count]:
                # Create a new root with left and right subtrees
                root = TreeNode(0, left, right)
                dp[count].append(root)
