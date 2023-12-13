class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        row_sum = [sum(row) for row in mat]
        col_sum = [0 for _ in range(n)]
        for i in range(n):
            for j in range(m):
                col_sum[i] += mat[j][i]
        
        res = 0
        for i in range(m):
            if row_sum[i] == 1:
                for j in range(n):
                    if mat[i][j] == 1:
                        if col_sum[j] == 1:
                            res += 1
                        break

        return res