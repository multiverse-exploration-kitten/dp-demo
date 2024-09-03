from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # find the total sum of the array
        tot_sum = sum(nums)

        # find the subset sum
        # because we split the array into 2 subsets
        # subset sum should be total sum divide by 2

        # if total sum is an odd number
        if tot_sum % 2 != 0:
            return False

        subset_sum = tot_sum // 2

        # dp matrix
        # from 0 -> subset sum
        # from including 0 element to all elements
        dp = [[False for _ in range(subset_sum + 1)] for _ in range(len(nums) + 1)]
        # base case
        # 0 element can sum to 0
        dp[0][0] = True

        # fill up the dp matrix
        # similar process as coin change & longest increasing subsequence
        for i in range(1, len(nums) + 1):
            # check the element in the array one by one
            curr_num = nums[i - 1]
            for curr_sum in range(subset_sum + 1):
                if curr_sum < curr_num:
                    # if the curren number is smaller than the target sum
                    # previous row, same entry
                    dp[i][curr_sum] = dp[i - 1][curr_sum]
                else:
                    # previous row, same entry or previous row - curr num
                    dp[i][curr_sum] = (
                        dp[i - 1][curr_sum] or dp[i - 1][curr_sum - curr_num]
                    )

        # last entry is the result
        return dp[-1][-1]
