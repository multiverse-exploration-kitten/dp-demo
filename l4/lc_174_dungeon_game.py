import sys
from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows, cols = len(dungeon), len(dungeon[0])
        dp = [[sys.maxsize] * cols for _ in range(rows)]

        for row in reversed(range(rows)):
            for col in reversed(range(cols)):
                curr_cell = dungeon[row][col]

                # Calculate the minimum health required for the cell to the right (if within bounds)
                if col + 1 < cols:
                    health_needed_if_move_right = dp[row][col + 1] - curr_cell
                    min_health_from_right = max(1, health_needed_if_move_right)
                else:
                    min_health_from_right = sys.maxsize

                # Calculate the minimum health required for the cell below (if within bounds)
                if row + 1 < rows:
                    health_needed_if_move_down = dp[row + 1][col] - curr_cell
                    min_health_from_below = max(1, health_needed_if_move_down)
                else:
                    min_health_from_below = sys.maxsize

                # Determine the minimum health required to move to either the right or below
                next_cell_min_health = min(min_health_from_right, min_health_from_below)

                # If it's the last cell (bottom-right), the hero needs at least 1 HP to survive
                if next_cell_min_health == sys.maxsize:
                    min_health = 1 if curr_cell >= 0 else 1 - curr_cell
                else:
                    min_health = next_cell_min_health

                dp[row][col] = min_health

        return dp[0][0]
