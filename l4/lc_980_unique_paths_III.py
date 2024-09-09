from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        walkable = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    x, y = (i, j)
                elif grid[i][j] == 0:
                    walkable += 1

        self.res = 0

        self.explore(grid, visited, x, y, walkable)

        return self.res

    def explore(self, grid, visited, x, y, walkable):
        if grid[x][y] == 2:
            if walkable + 1 == 0:
                self.res += 1
            return

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited[x][y] = True

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if not self.in_bound(nx, ny, grid):
                continue

            if grid[nx][ny] == -1:
                continue

            if visited[nx][ny]:
                continue

            self.explore(grid, visited, nx, ny, walkable - 1)
        visited[x][y] = False

        return

    def in_bound(self, x, y, grid):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])
