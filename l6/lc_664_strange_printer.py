class Solution:
    def strangePrinter(self, s: str) -> int:
        # Length of the string
        n = len(s)
        # Initialize the DP table with max possible operations
        dp = [[n] * n for _ in range(n)]

        # Iterate over every possible length of substrings
        for length in range(1, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1
                # Initialize variable to mark the last mismatch before right
                last_mismatch = -1
                # Check each character between left and right-1
                for i in range(left, right):
                    if s[i] != s[right] and last_mismatch == -1:
                        last_mismatch = i
                    if last_mismatch != -1:
                        # Calculate the minimum operations needed
                        dp[left][right] = min(
                            dp[left][right], 1 + dp[last_mismatch][i] + dp[i + 1][right]
                        )

                # If no mismatch found, it means all characters are same as 'right'
                if last_mismatch == -1:
                    dp[left][right] = 0

        # Adjust the result by adding 1 as per problem statement
        return dp[0][n - 1] + 1
