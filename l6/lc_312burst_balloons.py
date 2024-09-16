from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Handle special case where all numbers are the same and more than one exists
        if len(nums) > 1 and len(set(nums)) == 1:
            return (nums[0] ** 3) * (len(nums) - 2) + nums[0] ** 2 + nums[0]

        # Add padding balloons with value 1 on both ends
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        # Compute maximum coins by bursting all balloons between i and j
        for left in range(n - 2, 0, -1):
            for right in range(left, n - 1):
                for i in range(left, right + 1):
                    gain = nums[left - 1] * nums[i] * nums[right + 1]
                    remaining = dp[left][i - 1] + dp[i + 1][right]
                    dp[left][right] = max(dp[left][right], remaining + gain)

        # Return the max coins possible from bursting all balloons except the fake ones
        return dp[1][n - 2]
