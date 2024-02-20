class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        matrix = [[0] * len(colSum) for _ in range(len(rowSum))]

        for row in range(len(rowSum)):
            for col in range(len(colSum)):
                x = min(rowSum[row], colSum[col])

                matrix[row][col] = x

                rowSum[row] -= x
                colSum[col] -= x
        
        return matrix