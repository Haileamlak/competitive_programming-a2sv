# Problem: Nearest Exit from Entrance in Maze - https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def inbound(row, col):
            return (0 <= row < m) and (0 <= col < n)
        
        def is_exit(row, col):
            return (row == 0 or row == m - 1) or (col == 0 or col == n - 1)

        
        visited = [[False] * n for _ in range(m)]

        start_row, start_col = entrance
        visited[start_row][start_col] = True
        
        queue = deque()
        for i, j in directions:
            r, c = start_row + i, start_col + j
            if inbound(r, c) and maze[r][c] == '.':
                visited[r][c] = True
                queue.append((r, c))

        res = inf
        steps = 1
        while queue:
            print(queue)
            for _ in range(len(queue)):
                row, col = queue.popleft()

                if is_exit(row, col):
                    res = min(res, steps)
                
                for i, j in directions:
                    r, c = row + i, col + j
                    if inbound(r, c) and not visited[r][c] and maze[r][c] == '.':
                        visited[r][c] = True
                        queue.append((r, c))

            steps += 1

        return res if (res != inf) else -1