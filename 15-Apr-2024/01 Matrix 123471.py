# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = ((0, 1), (0, -1), (-1, 0), (1, 0))
        m, n = len(mat), len(mat[0])

        res = [[inf] * n for _ in range(m)]

        def inbound(row, col):
            return (0 <= row < m) and (0 <= col < n)

        queue = deque()
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0:
                    res[row][col] = 0
                    queue.append((row, col))

        distance = 1
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for i, j in directions:
                    r, c = row + i, col + j
                    if inbound(r, c) and res[r][c] == inf and mat[r][c] == 1:
                        res[r][c] = distance
                        queue.append((r, c))
            
            distance += 1

        return res