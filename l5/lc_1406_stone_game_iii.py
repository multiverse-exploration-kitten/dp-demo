from typing import List


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        # suffix_sum[i] stores the sum of stone values from index i to the end of the array.
        suffix_sum = [0 for _ in range(n + 1)]
        # dp[i] represents the maximum score difference (Alice's score - Bob's score) starting from index i.
        dp = [0 for _ in range(n + 1)]

        # Build the suffix sum array in reverse order.
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + stoneValue[i]

        # Build the dp array in reverse order.
        for i in range(n - 1, -1, -1):
            # The player can take the first stone, then the score difference is current stone plus remaining score difference.
            dp[i] = stoneValue[i] + suffix_sum[i + 1] - dp[i + 1]
            # Player can also take 2 or 3 stones, need to check all possibilities (up to 3 stones if possible).
            for k in range(i + 1, min(n, i + 3)):
                # Calculate the score difference if taking more stones and update dp[i] to the maximum possible value.
                dp[i] = max(dp[i], suffix_sum[i] - dp[k + 1])

        # The total score of all stones is suffix_sum[0].
        # If dp[0]*2 == suffix_sum[0], then the score is exactly divided between Alice and Bob.
        if dp[0] * 2 == suffix_sum[0]:
            return "Tie"
        # If dp[0] is greater than half of suffix_sum[0], Alice wins.
        elif dp[0] * 2 > suffix_sum[0]:
            return "Alice"
        # Otherwise, Bob wins.
        else:
            return "Bob"
