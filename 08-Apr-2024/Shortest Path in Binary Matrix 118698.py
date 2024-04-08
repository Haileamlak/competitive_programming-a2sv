# Problem: Shortest Path in Binary Matrix - https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
            
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1))
        m, n = len(grid), len(grid[0])

        def inbound(row, col):
            return (0 <= row < m) and (0 <= col < n)

        bottom_right = (m - 1, n - 1)

        res = float('inf')

        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True

        queue = deque([(0, 0, 1)])

        while queue:
            row, col, length = queue.popleft()
            if (row, col) == bottom_right:
                res = min(res, length)
            
            else:
                for i, j in directions:
                    new_row, new_col = row + i, col + j
                    if inbound(new_row, new_col) and grid[new_row][new_col] == 0 and not visited[new_row][new_col]:
                        queue.append((new_row, new_col, length + 1))
                        visited[new_row][new_col] = True
        
        return res if res < float('inf') else -1