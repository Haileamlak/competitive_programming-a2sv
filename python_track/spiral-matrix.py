class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        row, column = 0, 0
        m, n = len(matrix), len(matrix[0])
        while row < m and column < n:
            # the first row
            res.extend(matrix[row][column:n])

            if (m - row) == 1:
                break
            # the last column
            for r in range(row + 1, m - 1):
                res.append(matrix[r][n - 1])

            # the last row
            last_row = matrix[m - 1][column:n]
            res.extend(reversed(last_row))

            if (n - column) == 1:
                break
            # the first column
            for r in range(m - 2, row, -1):
                res.append(matrix[r][column])

            row += 1
            column += 1
            m -= 1
            n -= 1  


        # res.pop()
        return res

