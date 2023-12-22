class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        print(matrix)
        n = len(matrix)
        for row in range(n):
            for col in range(row, n):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        print(matrix)
        for row in range(n):
            col = 0
            end = n - 1
            while col < end:
                matrix[row][col], matrix[row][end] = matrix[row][end], matrix[row][col]

                col += 1
                end -= 1
