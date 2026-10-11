class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        n = len(matrix) # rows
        m = len(matrix[0]) # cols

        self.prefixMatrix = [[0] * (m+1) for _ in range(n + 1)] # create 2d array
        
        # create prefix matrix
        for r in range(n):
            prefix = 0
            for c in range(m):
                prefix += matrix[r][c]
                above = self.prefixMatrix[r][c + 1] # c + 1 because prefix padding
                self.prefixMatrix[r + 1][c + 1] = prefix + above # + 1 cause prefix padding



    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        # adjust row/col because prefix padding
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        bottomRight = self.prefixMatrix[row2][col2]
        above = self.prefixMatrix[row1 - 1][col2]
        left = self.prefixMatrix[row2][col1 - 1]
        topLeft = self.prefixMatrix[row1 - 1][col1 - 1]

        return bottomRight - above - left + topLeft