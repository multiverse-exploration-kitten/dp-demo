from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        # Create a 2D DP table with (n+1) rows for piles and (n+1) columns for possible values of M
        dp = [[0] * (n + 1) for _ in range(n + 1)]  # dp[i]
        # total_sum[i] will hold the total number of stones from pile i to the end of the array
        total_sum = [0] * (n + 1)  # prefix sum

        # Precompute total_sum in reverse to avoid recalculating sums repeatedly
        for i in range(n - 1, -1, -1):
            total_sum[i] = total_sum[i + 1] + piles[i]

        # Fill the DP table from right to left, which means from the end of the piles back to the start
        for i in range(n - 1, -1, -1):
            # Iterate through all possible values of M from 1 up to n
            for m in range(1, n + 1):
                # Calculate the maximum number of piles Alice can take, limited by 2*M and remaining piles
                max_piles = min(2 * m, n - i)
                # Try every possible number of piles `x` Alice could take starting from `i` with parameter `M`
                for x in range(1, max_piles + 1):
                    current_gain = sum(
                        piles[i : i + x]
                    )  # Stones Alice would gain by taking `x` piles
                    new_m = max(
                        m, x
                    )  # Update M to the maximum of current M or x, as rules dictate
                    # If taking these piles results in reaching the end of the array
                    if i + x >= n:
                        dp[i][m] = max(
                            dp[i][m], current_gain
                        )  # Alice takes all remaining piles
                    else:
                        # Recurrence relation: Alice's gain is her current gain plus the best she can do
                        # after Bob takes his turn starting from `i+x` with updated `M = new_m`
                        dp[i][m] = max(
                            dp[i][m],
                            current_gain
                            + (total_sum[i] - current_gain - dp[i + x][new_m]),
                        )

        # Return the maximum stones Alice can get starting from the first pile with M = 1
        return dp[0][1]
