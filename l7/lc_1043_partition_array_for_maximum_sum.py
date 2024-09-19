from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        arr_len = len(arr)
        dp = [0] * (arr_len + 1)

        for start in range(arr_len - 1, -1, -1):
            curr_max = 0
            end = min(arr_len, start + k)

            for i in range(start, end):
                curr_max = max(curr_max, arr[i])
                dp[start] = max(dp[start], dp[i + 1] + curr_max * (i - start + 1))

        return dp[0]
