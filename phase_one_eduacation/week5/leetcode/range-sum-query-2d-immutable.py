class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.pre_sum = matrix
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(1, m):
                self.pre_sum[i][j] = self.pre_sum[i][j - 1] + matrix[i][j]
        
        for i in range(m):
            for j in range(1, n):
                self.pre_sum[j][i] = self.pre_sum[j - 1][i] + matrix[j][i]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0 and col1 == 0:
            return self.pre_sum[row2][col2]
        
        elif row1 == 0:
            return self.pre_sum[row2][col2] - self.pre_sum[row2][col1 - 1]
        elif col1 == 0:
            return self.pre_sum[row2][col2] - self.pre_sum[row1 - 1][col2]
        
        return (self.pre_sum[row2][col2] - self.pre_sum[row2][col1 -1]) - (self.pre_sum[row1 - 1][col2] - self.pre_sum[row1 - 1][col1 - 1]) 

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)