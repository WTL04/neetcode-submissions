class NumMatrix:

    """
    1. calculate prefix sum of each row 

    """

    def __init__(self, matrix: List[List[int]]):

        n = len(matrix) # rows
        m = len(matrix[0]) # cols
        
        # create prefix matrix
        self.prefixMatrix = []
        for i in range(n):
            prefixRow = [0] * (m + 1)
            for j in range(m):
                prefixRow[j + 1] = prefixRow[j] + matrix[i][j]

            self.prefixMatrix.append(prefixRow)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # get num of rows
        total = 0
        for row in range(row1, row2 + 1):
            total += self.prefixMatrix[row][col2 + 1] - self.prefixMatrix[row][col1]
        return total