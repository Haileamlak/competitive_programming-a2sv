# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]
        for u, v, w in times:
            graph[u].append((v, w))

        res = 0
        visited = set()
        heap = [(0, k)]
         
        while heap:
            curr_time, node = heappop(heap)
            if node in visited:
                continue
            
            res = curr_time

            visited.add(node)
            for neighbor, time in graph[node]:
                if neighbor in visited:
                    continue

                heappush(heap, (time + curr_time, neighbor))
            
        return res if len(visited) == n else -1