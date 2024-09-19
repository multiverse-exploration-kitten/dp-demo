from typing import List


class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        num_len = len(nums)
        dp = [0] * (num_len + 1)

        for i in range(num_len):
            dp[i + 1] = dp[i] + nums[i]

        dp = [0.0] * num_len
        for i in range(num_len):
            dp[i] = (dp[num_len] - dp[i]) / (num_len - i)

        for k in range(k - 1):
            new_dp = dp[:]
            for i in range(num_len):
                for j in range(i + 1, num_len):
                    new_dp[i] = max(new_dp[i], (dp[j] - dp[i]) / (j - i) + dp[j])
            dp = new_dp

        return dp[0]
