# Problem: Shortest Path to Get All Keys - https://leetcode.com/problems/shortest-path-to-get-all-keys/

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        
        visited = [[[] for _ in range(n)] for _ in range(m)]

        queue = deque()
        keys_count = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == '@':
                    queue.append((row, col, 0))
                    visited[row][col].append(0)

                elif grid[row][col].islower():
                    keys_count += 1
        
        def inbound(row, col):
            return (0 <= row < m) and (0 <= col < n)
        
        def lock_with_no_key(row, col, keys):
            return (grid[row][col].isupper() and not keys & (1 << (ord(grid[row][col]) - ord('A'))))
        
        all_keys = pow(2, keys_count) - 1
        steps = 0
        while queue:
            for _ in range(len(queue)):
                row, col, curr_keys = queue.popleft()
                if curr_keys == all_keys:
                    return steps

                for i, j in directions:
                    new_row, new_col = row + i, col + j
                    if inbound(new_row, new_col) and grid[new_row][new_col] != '#' and not lock_with_no_key(new_row, new_col, curr_keys):
                        new_keys = curr_keys
                        if grid[new_row][new_col].islower():
                            new_keys |= (1 << (ord(grid[new_row][new_col]) - ord('a')))

                        if new_keys not in visited[new_row][new_col]:
                            visited[new_row][new_col].append(new_keys)
                            queue.append((new_row, new_col, new_keys))
                
            steps += 1
        
        return -1