# Problem: Count Sub Islands - https://leetcode.com/problems/count-sub-islands/

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        
        m, n = len(grid2), len(grid2[0])

        def inbound(row, col):
            return (0 <= row < m) and (0 <= col < n)

        def is_sub_island(row, col, visited):
            visited[row][col] = True

            res = (grid1[row][col] == 1)
            for i, j in directions:
                new_row, new_col = row + i, col + j
                
                if inbound(new_row, new_col) and not visited[new_row][new_col] and grid2[new_row][new_col] == 1:
                    res = is_sub_island(new_row, new_col, visited) and res
            
            return res

        visited = [[False] * n for _ in range(m)]
        
        ans = 0
        for row in range(m):
            for col in range(n):
                if not visited[row][col] and grid2[row][col] == 1 and is_sub_island(row, col, visited):
                    ans += 1

        return ans