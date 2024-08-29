class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_length = 0
        dp = [0] * len(s)

        for i in range(1, len(s)):
            if s[i] == ")":
                if s[i - 1] == "(":
                    # If the current ')' pairs with the previous '('
                    if i >= 2:
                        dp[i] = dp[i - 2] + 2
                    else:
                        dp[i] = 2
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == "(":
                    # If the current ')' pairs with a '(' before a valid parentheses substring
                    if i - dp[i - 1] >= 2:
                        dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
                    else:
                        dp[i] = dp[i - 1] + 2

                max_length = max(max_length, dp[i])

        return max_length
