class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def isValid(r, c):
            return r >= 0 and r < n and c >= 0 and c < m and grid[r][c] == "1"

        def dfs(r, c):
            if not isValid(r, c):
                return 

            grid[r][c] = "2" # marked as visited

            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        n = len(grid)
        m = len(grid[0])
        count = 0

        for r in range(n):
            for c in range(m):
                if grid[r][c] == "1":
                    dfs(r, c)
                    count += 1
                    
                    

        return count