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

        for end in range(n):
            for same_count in range(end + 1):
                dp[end][end][same_count] = (same_count + 1) * (same_count + 1)

        for length in range(1, n):
            for end in range(length, n):
                start = end - length

                for same_count in range(start + 1):
                    max_score = (same_count + 1) * (same_count + 1) + dp[start + 1][end][0]

                    for mid in range(start + 1, end + 1):
                        if boxes[mid] == boxes[start]:
                            max_score = max(max_score, dp[start + 1][mid - 1][0] + dp[mid][end][same_count + 1])

                    dp[start][end][same_count] = max_score

        return dp[0][n - 1][0] if n > 0 else 0
