import sys
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarray = -sys.maxsize

        current_subarray = 0

        for n in nums:
            current_subarray += n

            current_subarray = max(current_subarray, n)
            max_subarray = max(max_subarray, current_subarray)

        return max_subarray
