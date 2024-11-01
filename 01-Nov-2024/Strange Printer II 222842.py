# Problem: Strange Printer II - https://leetcode.com/problems/strange-printer-ii/

class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(targetGrid), len(targetGrid[0])

        colors = set()
        bound = {}
        for row in range(m):
            for col in range(n):
                color = targetGrid[row][col]
                if color not in bound:
                    colors.add(color)
                    bound[color] = [row, col, row, col]
                else:
                    bound[color][0] = min(bound[color][0], row)
                    bound[color][1] = min(bound[color][1], col)
                    bound[color][2] = max(bound[color][2], row)
                    bound[color][3] = max(bound[color][3], col)

        graph = [set() for _ in range(61)]
        indegree = defaultdict(int)
        
        for color in colors:
            for row in range(bound[color][0], bound[color][2] + 1):
                for col in range(bound[color][1], bound[color][3] + 1):
                    if targetGrid[row][col] != color and targetGrid[row][col] not in graph[color]:
                        graph[color].add(targetGrid[row][col])
                        indegree[targetGrid[row][col]] += 1

        queue = deque([color for color in colors if color not in indegree])

        res = 0
        while queue:
            curr = queue.popleft()
            for nbr in graph[curr]:
                indegree[nbr] -= 1
                
                if not indegree[nbr]:
                    queue.append(nbr)

            res += 1

        return res == len(colors)