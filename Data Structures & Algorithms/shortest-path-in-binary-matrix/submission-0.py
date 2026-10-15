class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1), 
                (-1, -1), (-1, 1), (1, -1), (1, 1)]

        def isValid(r, c):
            return r >= 0 and r < n and c >= 0 and c < n and grid[r][c] == 0

        def bfs(r, c, length):
            # edge case
            if grid[0][0] == 1 or grid[n-1][n-1] == 1:
                return -1

            queue = deque()
            queue.append((r, c, length)) # add start 
            grid[r][c] = 1 # set as visited

            while queue:
                # deque current node
                r, c, length = queue.popleft()

                if r == n -1 and c == n - 1:
                    return length

                # find neighbors of current node
                for dr, dc in dirs:
                    next_r = r + dr
                    next_c = c + dc

                    if isValid(next_r, next_c):
                        queue.append((next_r, next_c, length+1)) # add neighbor
                        grid[next_r][next_c] = 1 # set as visited
            return -1

        return bfs(0, 0, 1)
    