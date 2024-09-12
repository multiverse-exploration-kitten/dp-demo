class Solution:
    def canWin(self, currentState: str) -> bool:
        return self.canWinRecursive(currentState)

    def canWinRecursive(self, state: str) -> bool:
        # Iterate through the string to find all possible "++" flips
        for i in range(len(state) - 1):
            # Check if two consecutive '+' can be flipped
            if state[i : i + 2] == "++":
                # Create a new state by flipping "++" to "--"
                flipped_state = state[:i] + "--" + state[i + 2 :]
                # If the opponent cannot win after this flip, return True
                if not self.canWinRecursive(flipped_state):
                    return True

        # If no flip leads to a win for the current player, return False
        return False
