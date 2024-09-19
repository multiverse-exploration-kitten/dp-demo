import sys
from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        dp = [[0] * (m + 1) for _ in range(n)]

        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        for subarray_count in range(1, m + 1):
            for curr_index in range(n):
                if subarray_count == 1:
                    dp[curr_index][subarray_count] = (
                        prefix_sum[n] - prefix_sum[curr_index]
                    )
                    continue

                min_largest_split_sum = sys.maxsize
                for split_index in range(curr_index, n - subarray_count + 1):
                    current_subarray_sum = (
                        prefix_sum[split_index + 1] - prefix_sum[curr_index]
                    )
                    largest_split_sum = max(
                        current_subarray_sum, dp[split_index + 1][subarray_count - 1]
                    )

                    min_largest_split_sum = min(
                        min_largest_split_sum, largest_split_sum
                    )

                    if current_subarray_sum >= min_largest_split_sum:
                        break

                dp[curr_index][subarray_count] = min_largest_split_sum

        return dp[0][m]
