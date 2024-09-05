from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Initialize a list to keep track of the number of ways to reach each sum up to the target
        dp = [0] * (target + 1)
        dp[0] = 1  # Base case: one way to make the sum 0 (use no numbers)

        # Iterate over all possible sums from 1 to the target
        for current_sum in range(1, target + 1):
            # Check each number in the input list
            for num in nums:
                # If the number can be used to reach the current sum
                if current_sum >= num:
                    dp[current_sum] += dp[current_sum - num]

        return dp[target]
