# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        for i in range(len(queries)):
            queries[i].append(i)

        parent = {}
        size = {}

        def find(query):
            if query not in parent:
                parent[query] = query
                size[query] = 1
            
            while query != parent[query]:
                parent[query] = parent[parent[query]]
                query = parent[query]
            
            return query

        def union(edge1, edge2):
            parent1 = find(edge1)
            parent2 = find(edge2)

            if size[parent1] > size[parent2]:
                parent[parent2] = parent1
                size[parent1] += size[parent2]
            else:
                parent[parent1] = parent2
                size[parent2] += size[parent1]
        
        def are_connected(node1, node2):
            return find(node1) == find(node2)

        answer = [False] * len(queries)

        queries.sort(key = lambda query : query[2])

        edgeList.sort(key = lambda edge : edge[2])


        i = 0
        for query in queries:
            node1, node2, curr_limit, index = query
            while i < len(edgeList) and edgeList[i][2] < curr_limit:

                union(edgeList[i][0], edgeList[i][1])

                i += 1

            answer[index] = are_connected(node1, node2)
        
        return answer