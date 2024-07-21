# Problem: Build a Matrix With Conditions - https://leetcode.com/problems/build-a-matrix-with-conditions/

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        def topological_sort(conditions):
            
            graph = defaultdict(list)
            indegree = defaultdict(int)

            for a, b in conditions:
                graph[a].append(b)
                indegree[b] += 1

            res = []
            queue = deque([num for num in range(1, k + 1) if num not in indegree])
            
            while queue:
                curr = queue.popleft()
                res.append(curr)

                for neighbour in graph[curr]:
                    indegree[neighbour] -= 1

                    if indegree[neighbour] == 0:
                        queue.append(neighbour)
            
            return res
        
        sorted_row = topological_sort(rowConditions)
        
        if len(sorted_row) != k:
            return []
        
        sorted_col = topological_sort(colConditions)

        if len(sorted_col) != k:
            return []
        
        answer = [[0] * k for _ in range(k)]

        for row in range(k):
            for col in range(k):
                if sorted_row[row] == sorted_col[col]:
                    answer[row][col] = sorted_row[row]
        
        return answer