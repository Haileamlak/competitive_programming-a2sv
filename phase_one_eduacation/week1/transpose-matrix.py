class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])

        transpose = []
        for i in range(n):
            transpose.append([])
            for j in range(m):
                transpose[i].append(matrix[j][i])
        
        return transpose