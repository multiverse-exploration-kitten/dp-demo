from typing import List


class SolutionTopDown:
    def removeBoxes(self, boxes: List[int]) -> int:
        # Create a 3D list initialized with None to store memoization results
        n = len(boxes)
        dp = [[[None] * n for _ in range(n)] for __ in range(n)]
        return self.calculate_points(boxes, dp, 0, n - 1, 0)

    def calculate_points(self, boxes, dp, l, r, k):
        if l > r:
            return 0

        # Consolidate consecutive boxes of the same type
        while r > l and boxes[r] == boxes[r - 1]:
            r -= 1
            k += 1

        # Use memoization to avoid recalculating the same scenario
        if dp[l][r][k] is not None:
            return dp[l][r][k]

        # Compute the points for the current configuration
        dp[l][r][k] = self.calculate_points(boxes, dp, l, r - 1, 0) + (k + 1) ** 2
        for i in range(l, r):
            if boxes[i] == boxes[r]:
                dp[l][r][k] = max(
                    dp[l][r][k],
                    self.calculate_points(boxes, dp, l, i, k + 1)
                    + self.calculate_points(boxes, dp, i + 1, r - 1, 0),
                )

        return dp[l][r][k]


class SolutionBottomUp:
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)
        dp = [[[0] * n for _ in range(n)] for _ in range(n)]

        for j in range(n):
            for k in range(j + 1):
                dp[j][j][k] = (k + 1) * (k + 1)

        for l in range(1, n):
            for j in range(l, n):
                i = j - l

                for k in range(i + 1):
                    res = (k + 1) * (k + 1) + dp[i + 1][j][0]

                    for m in range(i + 1, j + 1):
                        if boxes[m] == boxes[i]:
                            res = max(res, dp[i + 1][m - 1][0] + dp[m][j][k + 1])

                    dp[i][j][k] = res

        return dp[0][n - 1][0] if n > 0 else 0
