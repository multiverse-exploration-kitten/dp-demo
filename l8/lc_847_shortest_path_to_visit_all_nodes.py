import sys
from collections import deque
from typing import List


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:

        n = len(graph)

        # Define the dp array: dp[mask][i] represents the shortest path length
        # when visiting nodes indicated by "mask" and currently at node "i"
        dp = [[sys.maxsize] * n for _ in range(1 << n)]

        # Initialize the queue. Initially, we can start visiting from any node.
        queue = deque()

        # Initialization: Start from each node as the starting point
        for i in range(n):
            dp[1 << i][i] = 0  # Initial state: only the i-th node is visited
            queue.append((1 << i, i))  # (mask, current node)

        # BFS
        while queue:
            mask, u = queue.popleft()

            # Traverse the neighbors of node u
            for v in graph[u]:
                # Calculate the new state: next_mask represents the new set of visited nodes, including node v
                next_mask = mask | (1 << v)  # Add the v-th node to the visited set

                # If visiting the new state (next_mask) from the current path provides a shorter path, update dp
                if dp[next_mask][v] > dp[mask][u] + 1:
                    dp[next_mask][v] = dp[mask][u] + 1
                    queue.append((next_mask, v))

        # Find the shortest path where all nodes are visited, i.e., mask = (1 << n) - 1
        # Create a bitmask with all n nodes visited
        final_mask = (1 << n) - 1
        return min(dp[final_mask][i] for i in range(n))
