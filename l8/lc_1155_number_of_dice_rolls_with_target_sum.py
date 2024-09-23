class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 1000000007
        memo = [[0] * (target + 1) for _ in range(n + 1)]

        # Initialize the base case
        memo[n][target] = 1

        for dice_index in range(n - 1, -1, -1):
            for curr_sum in range(target + 1):
                ways = 0

                # Iterate over the possible face values for the current die
                for i in range(1, min(k, target - curr_sum) + 1):
                    ways = (ways + memo[dice_index + 1][curr_sum + i]) % MOD

                memo[dice_index][curr_sum] = ways

        return memo[0][0]
