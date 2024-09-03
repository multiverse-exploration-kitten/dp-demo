from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #  Calculate the total sum of the input numbers
        total_sum = sum(nums)

        # Edge case: If the absolute value of the target is greater than the total sum, it's impossible to achieve the target
        if abs(target) > total_sum:
            return 0

        # Initialize the DP table with dimensions [number of elements][2 * total_sum + 1]
        # We use a shift of total_sum to handle negative indices
        num_count = len(nums)
        dp = [[0] * (2 * total_sum + 1) for _ in range(num_count)]

        # Base case: At the first index, we can either add or subtract the first number
        dp[0][nums[0] + total_sum] = 1
        dp[0][-nums[0] + total_sum] += 1

        # Fill the DP table
        for i in range(1, num_count):
            for current_sum in range(-total_sum, total_sum + 1):
                shifted_index = current_sum + total_sum
                if dp[i - 1][shifted_index] > 0:
                    # Update the DP table for both adding and subtracting the current number
                    dp[i][shifted_index + nums[i]] += dp[i - 1][shifted_index]
                    dp[i][shifted_index - nums[i]] += dp[i - 1][shifted_index]

        # The result is the number of ways to achieve the target sum, shifted by total_sum
        return dp[num_count - 1][target + total_sum]
