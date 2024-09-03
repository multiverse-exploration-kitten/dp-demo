from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for s in strs:
            num_of_zeros = s.count("0")
            num_of_ones = s.count("1")

            for i in range(m, num_of_zeros - 1, -1):
                for j in range(n, num_of_ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - num_of_zeros][j - num_of_ones] + 1)

        return dp[m][n]