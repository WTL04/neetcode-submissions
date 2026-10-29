class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        '''
        bfs because we are looking for shortest path
        '''

        n = len(grid)
        m = len(grid[0])

        def isValid(r, c):
            return r >= 0 and r < n and c >= 0 and c < m and grid[r][c] != 'X'


        # find starting position
        for r in range(n):
            for c in range(m):
                if grid[r][c] == '*':
                    start_r = r
                    start_c = c


        # bfs
        from collections import deque
        q = deque()
        q.append((start_r, start_c, 0)) # (row, col, moves from start)
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:
            curr_r, curr_c, moves = q.popleft()

            for dr, dc in dirs:
                nr = curr_r + dr
                nc = curr_c + dc

                # add valid neighbors
                if isValid(nr, nc):
                    
                    # check for food
                    if grid[nr][nc] == '#':
                        return moves + 1

                    q.append((nr, nc, moves+1))
                    
                    # mark neighbors as visited 
                    grid[nr][nc] = 'X'
                    

        return -1 
        



