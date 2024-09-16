import sys
from typing import List


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        """Calculates the minimum cost of making cuts on a stick with given lengths."""
        num_cuts = len(cuts)
        cuts = [0] + sorted(cuts) + [n]

        # Create a dynamic programming table initialized to zero
        dp = [[0] * (num_cuts + 2) for _ in range(num_cuts + 2)]

        # Fill the DP table
        for diff in range(2, num_cuts + 2):
            for left in range(num_cuts + 2 - diff):
                right = left + diff
                min_cost = sys.maxsize
                for mid in range(left + 1, right):
                    min_cost = min(
                        min_cost,
                        dp[left][mid] + dp[mid][right] + cuts[right] - cuts[left],
                    )
                dp[left][right] = min_cost

        return dp[0][num_cuts + 1]
