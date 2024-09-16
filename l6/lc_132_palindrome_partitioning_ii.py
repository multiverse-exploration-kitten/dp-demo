import sys


class Solution:
    def minCut(self, s: str) -> int:
        # Step 1: Initialize the palindrome table
        n = len(s)
        is_palindrome = self.build_palindrome_table(s, n)

        # Step 2: Initialize DP array to track the minimum cuts
        dp = [sys.maxsize] * (n + 1)
        dp[0] = 0  # No cut needed for an empty string
        dp[1] = 0  # No cut needed for a single character string

        # Step 3: Calculate the minimum cuts needed
        for i in range(1, n + 1):
            for j in range(i):
                if is_palindrome[j][i - 1]:
                    if j == 0:
                        dp[i] = min(
                            dp[i], 0
                        )  # No cut needed if the whole substring is a palindrome
                    else:
                        dp[i] = min(dp[i], dp[j] + 1)

        # Step 4: Return the result from the dp array
        return dp[n]

    def build_palindrome_table(self, s: str, n: int):
        """
        Builds a table to track whether substrings s[i:j] are palindromes.
        """
        is_palindrome = [[False] * n for _ in range(n)]

        for i in range(n):
            is_palindrome[i][i] = True  # Every single character is a palindrome

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2 or is_palindrome[i + 1][j - 1]:
                        is_palindrome[i][j] = True

        return is_palindrome
