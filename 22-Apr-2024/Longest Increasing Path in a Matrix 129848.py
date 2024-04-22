# Problem: Longest Increasing Path in a Matrix - https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        indegree = [[0 for _ in range(n)] for _ in range(m)]

        def inbound(row, col):
            return (0 <= row < m) and (0 <= col < n)

        def indegree_count(row, col):
            res = 0
            for i, j in directions:
                new_row, new_col = row + i, col + j

                if inbound(new_row, new_col) and matrix[new_row][new_col] < matrix[row][col]:
                    res += 1
            
            return res

        for row in range(m):
            for col in range(n):
                indegree[row][col] = indegree_count(row, col)
        
        queue = deque([(row, col) for row in range(m) for col in range(n) if indegree[row][col] == 0])

        length = 0
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for i, j in directions:
                    new_row, new_col = row + i, col + j

                    if inbound(new_row, new_col) and matrix[new_row][new_col] > matrix[row][col]:
                        indegree[new_row][new_col] -= 1

                        if indegree[new_row][new_col] == 0:
                            queue.append((new_row, new_col))

            length += 1

        return length