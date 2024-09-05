from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
        dp[0][0] = 1

        for i in range(1, len(coins) + 1):
            dp[i][0] = 1
            for j in range(1, amount + 1):
                curr_coin = coins[i - 1]
                if j >= curr_coin:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - curr_coin]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[-1][-1]

        # # space optimization
        # dp = [0 for _ in range(amount + 1)]
        # dp[0] = 1

        # for coin in coins:
        #     for i in range(1, amount + 1):
        #         if coin <= i:
        #             dp[i] += dp[i - coin]

        # return dp[-1]
