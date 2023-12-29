class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        res = 0
        for row in range(n):
            res += mat[row][row] + mat[row][n - row - 1]
        
        if n % 2 == 1:
            res -= mat[n//2][n//2]
        
        return res
            
        
        