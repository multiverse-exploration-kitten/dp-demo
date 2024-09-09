from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        if len(grid[0]) == 0:
            return 0

        dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        for i in range(len(grid)):
            if i > 0:
                dp[i][0] = dp[i - 1][0] + grid[i][0]
            else:
                dp[i][0] = grid[i][0]

        for j in range(len(grid[0])):
            if j > 0:
                dp[0][j] = dp[0][j - 1] + grid[0][j]
            else:
                dp[0][j] = grid[0][j]

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]

        return dp[-1][-1]
