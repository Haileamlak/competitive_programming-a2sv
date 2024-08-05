# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj_list = [[] for _ in range(n)]
        in_degree = defaultdict(int)

        for u, v in edges:
            adj_list[u].append(v)
            in_degree[v] += 1
        
        answer = [set() for _ in range(n)]

        queue = deque([node for node in range(n) if node not in in_degree])

        while queue:
            curr_node = queue.popleft()
            
            for child in adj_list[curr_node]:
                answer[child].add(curr_node)
                answer[child] = answer[child].union(answer[curr_node])

                in_degree[child] -= 1
                
                if in_degree[child] == 0:
                    queue.append(child)
        
        for node in range(n):
            answer[node] = list(sorted(answer[node]))

        return answer