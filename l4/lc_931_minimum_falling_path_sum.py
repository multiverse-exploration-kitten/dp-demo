import sys
from typing import List


class Solution:
    def minFallingPathSum(self, matrix):
        rows, cols = len(matrix), len(matrix[0])

        if rows == 1 or cols == 1:
            return matrix[0][0]

        dp = [[sys.maxsize] * cols for _ in range(rows)]
        result = sys.maxsize

        for i in range(len(matrix)):
            result = min(result, self.min_falling_path_sum_helper(matrix, 0, i, dp))

        return result

    def min_falling_path_sum_helper(
        self, matrix: List[List[int]], row: int, col: int, dp: List[List[int]]
    ) -> int:
        rows, cols = len(matrix), len(matrix[0])

        if dp[row][col] != sys.maxsize:
            return dp[row][col]

        if row == rows - 1:
            return matrix[row][col]

        left = right = sys.maxsize

        if col > 0:
            left = self.min_falling_path_sum_helper(matrix, row + 1, col - 1, dp)

        straight = self.min_falling_path_sum_helper(matrix, row + 1, col, dp)

        if col < cols - 1:
            right = self.min_falling_path_sum_helper(matrix, row + 1, col + 1, dp)

        dp[row][col] = min(left, min(straight, right)) + matrix[row][col]

        return dp[row][col]
