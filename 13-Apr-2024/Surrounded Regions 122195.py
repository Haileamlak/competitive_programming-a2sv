# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def out_of_bound(row, col):
            return (row < 0 or row >= m) or (col < 0 or col >= n)

        def dfs(row, col, visited):
            visited[row][col] = True

            for i, j in directions:
                new_row, new_col = row + i, col + j

                if not out_of_bound(new_row, new_col) and (board[new_row][new_col] == 'O') and (not visited[new_row][new_col]):
                    dfs(new_row, new_col, visited)
            
        m, n = len(board), len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]


        for row in range(m):
            if board[row][0] == 'O' and not visited[row][0]:
                dfs(row, 0, visited)

        for row in range(m):
            if board[row][n - 1] == 'O' and not visited[row][n - 1]:
                dfs(row, n - 1, visited)

        for col in range(n):
            if board[0][col] == 'O' and not visited[0][col]:
                dfs(0, col, visited)
        
        for col in range(n):
            if board[m - 1][col] == 'O' and not visited[m - 1][col]:
                dfs(m - 1, col, visited)


        def capture(row, col):
            board[row][col] = 'X'
            
            for i, j in directions:
                new_row, new_col = row + i, col + j
                if board[new_row][new_col] == 'O':
                    capture(new_row, new_col)

        for row in range(m):
            for col in range(n):
                if board[row][col] == 'O' and not visited[row][col]:
                    capture(row, col)