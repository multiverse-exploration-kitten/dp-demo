from typing import List


class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        arr_len = len(nums)
        prefix_sum = [0] * (arr_len + 1)

        for i in range(arr_len):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        dp = [[0.0 for _ in range(arr_len)] for _ in range(k)]
        for i in range(arr_len):
            dp[0][i] = (prefix_sum[arr_len] - prefix_sum[i]) / (arr_len - i)

        for k_idx in range(1, k):

            for i in range(arr_len):
                for j in range(i + 1, arr_len):
                    dp[k_idx][i] = max(
                        dp[k_idx][i],
                        (prefix_sum[j] - prefix_sum[i]) / (j - i) + dp[k_idx - 1][j],
                    )

        return dp[-1][0]


class SolutionCompressed:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        arr_len = len(nums)
        prefix_sum = [0] * (arr_len + 1)

        for i in range(arr_len):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        dp = [0.0] * arr_len
        for i in range(arr_len):
            dp[i] = (prefix_sum[arr_len] - prefix_sum[i]) / (arr_len - i)

        for _ in range(k - 1):
            new_dp = dp[:]
            for i in range(arr_len):
                for j in range(i + 1, arr_len):
                    new_dp[i] = max(
                        new_dp[i], (prefix_sum[j] - prefix_sum[i]) / (j - i) + dp[j]
                    )
            dp = new_dp

        return dp[0]
