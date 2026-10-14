class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def isValid(r, c):
            return r >= 0 and r < n and c >= 0 and c < m and grid[r][c] == 1

        def dfs(r, c):
            if not isValid(r, c):
                return 0

            grid[r][c] = 2 # marked as visited

            return 1 + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1)
            
        n = len(grid)
        m = len(grid[0])
        maxArea = 0

        for r in range(n):
            for c in range(m):
                    islandArea = dfs(r, c)
                    maxArea = max(islandArea, maxArea)
        return maxArea
