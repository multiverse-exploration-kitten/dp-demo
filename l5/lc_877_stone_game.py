class Solution:
    def stoneGame(self, piles):
        # Number of piles
        num_piles = len(piles)

        # Initialize a 2D dp array where dp[i][j] represents the maximum score difference
        # the current player can achieve starting from piles[i] to piles[j]
        dp = [[0] * num_piles for _ in range(num_piles)]

        # Base case: when i == j, there's only one pile to take
        for i in range(num_piles):
            dp[i][i] = piles[i]

        # Solve for ranges of increasing lengths (from 2 piles to num_piles)
        for length in range(2, num_piles + 1):
            for i in range(num_piles - length + 1):
                j = i + length - 1  # Calculate the end index of the subarray

                # Calculate parity to check whose turn it is: 1 for the first player, 0 for the second
                is_first_player_turn = (j - i - num_piles) % 2 == 1

                if is_first_player_turn:
                    # First player tries to maximize their score by picking either the first or last pile
                    dp[i][j] = max(piles[i] + dp[i + 1][j], piles[j] + dp[i][j - 1])
                else:
                    # Second player minimizes the first player's score by choosing a pile
                    dp[i][j] = min(-piles[i] + dp[i + 1][j], -piles[j] + dp[i][j - 1])

        # If the score difference is positive, the first player wins
        return dp[0][num_piles - 1] > 0
