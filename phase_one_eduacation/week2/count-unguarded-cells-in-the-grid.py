# class Solution:
#     def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
#         grid = [['e' for _ in range(n)] for _ in range(m)]

#         # for guard in guards:
#         #     grid[guard[0]][guard[1]] = 'g'

#         for wall in walls:
#             grid[wall[0]][wall[1]] = 'w'
        
#         for guard in guards:
#             grid[guard[0]][guard[1]] = 'G'

#             row, col = guard[0] - 1, guard[1]

#             while row >= 0 and (grid[row][col] == 'e' or grid[row][col] == 'g'):
#                 grid[row][col] = 'g'
#                 row -= 1

#             row, col = guard[0], guard[1] - 1

#             while col >= 0 and (grid[row][col] == 'e' or grid[row][col] == 'g'):
#                 grid[row][col] = 'g'
#                 col -= 1
            
#             row, col = guard[0] + 1, guard[1]

#             while row < m and (grid[row][col] == 'e' or grid[row][col] == 'g'):
#                 grid[row][col] = 'g'
#                 row += 1
            
#             row, col = guard[0], guard[1] + 1

#             while col < n and (grid[row][col] == 'e' or grid[row][col] == 'g'):
#                 grid[row][col] = 'g'
#                 col += 1

#         res = 0
#         for row in range(m):
#             for col in range(n):
#                 if grid[row][col] == 'e':
#                     res += 1
                
#         return res

# from collections import namedtuple
# from typing import List

class Solution:

    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        Directions = namedtuple('Directions', ['x', 'y'])
        up = Directions(-1, 0)
        down = Directions(1, 0)
        left = Directions(0, -1)
        right = Directions(0, 1)

        matrix = [[0 for _ in range(n)] for _ in range(m)]
        for x, y in guards:
            matrix[x][y] = 'G'
        for x, y in walls:
            matrix[x][y] = 'W'

        def dfs(row, col, direction):
            if row < 0 or row >= m or col < 0 or col >= n or matrix[row][col] == 'W' or matrix[row][col] == 'G':
                return

            matrix[row][col] = 'X'
            dfs(row + direction.x, col + direction.y, direction)

        for x in range(m):
            for y in range(n):
                if matrix[x][y] == 'G':
                    dfs(x + 1, y, down)
                    dfs(x - 1, y, up)
                    dfs(x, y + 1, right)
                    dfs(x, y - 1, left)

        counter = 0
        for x in range(m):
            for y in range(n):
                if matrix[x][y] == 0:
                    counter += 1

        return counter
