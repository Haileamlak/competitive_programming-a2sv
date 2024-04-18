# Problem: Shortest Path to Get All Keys - https://leetcode.com/problems/shortest-path-to-get-all-keys/

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        
        visited = defaultdict(list)
        queue = deque()
        keys_count = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == '@':
                    queue.append((row, col, set()))
                    visited[(row, col)].append(set())

                elif grid[row][col].islower():
                    keys_count += 1
        
        def inbound(row, col):
            return (0 <= row < m) and (0 <= col < n)
        
        def lock_with_no_key(row, col, keys):
            return (grid[row][col].isupper() and grid[row][col].lower() not in keys)
        
        steps = 0
        while queue:
            for _ in range(len(queue)):
                row, col, curr_keys = queue.popleft()
                if len(curr_keys) == keys_count:
                    return steps

                for i, j in directions:
                    new_row, new_col = row + i, col + j
                    if inbound(new_row, new_col) and grid[new_row][new_col] != '#' and not lock_with_no_key(new_row, new_col, curr_keys):
                        new_keys = curr_keys.copy()
                        if grid[new_row][new_col].islower():
                            new_keys.add(grid[new_row][new_col])

                        if new_keys not in visited[(new_row, new_col)]:
                            visited[(new_row, new_col)].append(new_keys)
                            queue.append((new_row, new_col, new_keys))
                
            steps += 1
        
        return -1