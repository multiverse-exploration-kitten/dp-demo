import collections
from typing import List


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:

        # Count the frequency of each character in the target string
        t_count = collections.Counter(target)

        # Preprocess stickers: Keep only the characters that are also in the target
        # This will help optimize the sticker selection later
        A = [collections.Counter(sticker) & t_count for sticker in stickers]

        # Remove redundant stickers
        # If sticker A[i] is a subset of sticker A[j], we can discard A[i]
        for i in range(len(A) - 1, -1, -1):
            if any(A[i] == A[i] & A[j] for j in range(len(A)) if i != j):
                A.pop(i)

        # Convert the list of sticker counters back to their string form
        stickers = ["".join(s_count.elements()) for s_count in A]

        # dp[state] represents the minimum number of stickers needed to achieve a particular state
        # State is represented by a bitmask of length equal to the target string
        dp = [-1] * (1 << len(target))
        dp[0] = 0  # The base case: 0 stickers are needed to match an empty target

        # Iterate over all possible states
        for state in range(1 << len(target)):
            if dp[state] == -1:
                continue  # Skip invalid states (unreachable states)

            # Try each sticker to see how it can contribute to the current state
            for sticker in stickers:
                now = state  # Start from the current state
                for letter in sticker:
                    # Try to match each letter in the sticker with the target
                    for i, c in enumerate(target):
                        # If the i-th character of target is already matched in 'now', skip it
                        if (now >> i) & 1:
                            continue
                        # If the current letter matches the i-th character in target, mark it as matched
                        if c == letter:
                            # Use bitmask to mark the i-th character as completed
                            now |= (1 << i)
                            break

                # Update dp for the new state 'now'
                if dp[now] == -1 or dp[now] > dp[state] + 1:
                    dp[now] = dp[state] + 1

        # Return the minimum stickers needed to match all characters in target
        # The last state (all bits set) represents the full target matched
        return dp[-1]
