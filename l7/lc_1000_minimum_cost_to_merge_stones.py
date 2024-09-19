import sys
from typing import List


class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if (n - 1) % (k - 1) != 0:
            return -1

        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + stones[i - 1]

        # 3D DP table: dp[start][end][m]
        # dp[start][end][m] stores the minimum cost to merge stones from index `start` to `end` into `m` piles
        dp = [[[sys.maxsize] * (k + 1) for _ in range(n + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            dp[i][i][1] = 0

        for length in range(2, n + 1):
            for i in range(1, n - length + 2):
                j = i + length - 1

                for m in range(2, k + 1):
                    for t in range(i, j):
                        dp[i][j][m] = min(
                            dp[i][j][m], dp[i][t][m - 1] + dp[t + 1][j][1]
                        )

                dp[i][j][1] = dp[i][j][k] + prefix_sum[j] - prefix_sum[i - 1]

        return dp[1][n][1]
