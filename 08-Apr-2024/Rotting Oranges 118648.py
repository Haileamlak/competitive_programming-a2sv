# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        count = 0
        queue = deque()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row, col, 0))
                elif grid[row][col] == 1:
                    count += 1
        
        if not count:
            return 0
        
        def inbound(row, col):
            return (0 <= row < len(grid)) and (0 <= col < len(grid[0]))

        res = 0
        while queue:
            row, col, level = queue.popleft()

            res = max(res, level)

            for i, j in directions:
                r, c = row + i, col + j
                if inbound(r, c) and grid[r][c] == 1:
                    grid[r][c] = 2
                    queue.append((r, c, level + 1))
                    count -= 1

        return res if count == 0 else -1